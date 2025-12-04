#!/usr/bin/env python3
"""
Create a backup MOTD notice file if within threshold of next monthly backup.

This script calculates the first Sunday of the next month and creates a
markdown MOTD file 5 days before that date if we're within the threshold.
"""

import argparse
import datetime
import os
import sys
from pathlib import Path

DAY_THRESHOLD = 5


def next_first_sunday(today):
    """
    Find the next first Sunday of a month.

    Args:
        today: datetime.date object for the current date

    Returns:
        datetime.date object for the first Sunday of the current or next month
    """

    def first_sunday_of_month(year, month):
        """Helper to find first Sunday of a given month."""
        first_day = datetime.date(year, month, 1)
        # weekday(): Monday=0, Sunday=6
        days_until_sunday = (6 - first_day.weekday()) % 7
        first_sunday = first_day + datetime.timedelta(days=days_until_sunday)
        # If calculation goes beyond day 7, it means the month started on Sunday
        # In that case, the first Sunday is day 1
        if first_sunday.day > 7:
            first_sunday = first_day
        return first_sunday

    # Check current month first
    current_first_sunday = first_sunday_of_month(today.year, today.month)
    if current_first_sunday > today:
        return current_first_sunday

    # If current month's first Sunday has passed, get next month's
    if today.month == 12:
        next_year = today.year + 1
        next_month = 1
    else:
        next_year = today.year
        next_month = today.month + 1

    return first_sunday_of_month(next_year, next_month)


def render_template(template_path, context):
    """
    Render a Jinja2 template with the given context.

    Args:
        template_path: Path to the template file
        context: Dictionary of template variables

    Returns:
        Rendered template string
    """
    try:
        from jinja2 import Environment, FileSystemLoader

        template_dir = Path(template_path).parent
        template_name = Path(template_path).name

        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template(template_name)

        return template.render(**context)
    except ImportError:
        print(
            "Error: jinja2 package is required. Install with: pip install jinja2",
            file=sys.stderr,
        )
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Create backup MOTD notice if within threshold"
    )
    parser.add_argument(
        "--template",
        default=".github/templates/backup-motd.md.j2",
        help="Path to Jinja2 template file",
    )
    parser.add_argument(
        "--output-dir", default="motd", help="Directory to write MOTD files"
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=DAY_THRESHOLD,
        help=f"Days before backup to create notice (default: {DAY_THRESHOLD})",
    )
    parser.add_argument(
        "--force", action="store_true", help="Force creation even if outside threshold"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without creating files",
    )

    args = parser.parse_args()

    today = datetime.date.today()
    backup_date = next_first_sunday(today)
    days_until = (backup_date - today).days

    # Calculate notice date (threshold days before backup)
    notice_date = backup_date - datetime.timedelta(days=args.threshold)
    days_until_notice = (notice_date - today).days

    print(f"Today: {today.strftime('%Y-%m-%d (%A)')}")
    print(f"Next backup date: {backup_date.strftime('%Y-%m-%d (%A)')}")
    print(f"Notice date: {notice_date.strftime('%Y-%m-%d (%A)')}")
    print(f"Days until notice: {days_until_notice}")
    print(f"Days until backup: {days_until}")

    # Create the notice only on or shortly after the notice date
    # Too early: not yet within threshold
    if days_until > args.threshold and not args.force:
        print(
            f"Not within threshold ({days_until} > {args.threshold}). No action needed."
        )
        # Set GitHub Actions output
        if "GITHUB_OUTPUT" in os.environ:
            with open(os.environ["GITHUB_OUTPUT"], "a") as f:
                f.write("created=false\n")
        sys.exit(0)

    # Too late: we're more than 1 day past the notice date (missed the window)
    # Allow 1 day grace period for the automation to catch it
    if days_until_notice < -1 and not args.force:
        print(
            f"Past notice date window (notice was {-days_until_notice} days ago). No action needed."
        )
        # Set GitHub Actions output
        if "GITHUB_OUTPUT" in os.environ:
            with open(os.environ["GITHUB_OUTPUT"], "a") as f:
                f.write("created=false\n")
        sys.exit(0)
    filename = f"{notice_date.strftime('%Y-%m-%d')}-backups.md"
    filepath = Path(args.output_dir) / filename

    # Check if file already exists
    if filepath.exists():
        print(f"File {filepath} already exists. Nothing to do.")
        if "GITHUB_OUTPUT" in os.environ:
            with open(os.environ["GITHUB_OUTPUT"], "a") as f:
                f.write("created=false\n")
        sys.exit(0)

    # Prepare template context
    formatted_date = backup_date.strftime("%A, %B %e")
    hide_after = backup_date + datetime.timedelta(days=7)

    context = {
        "notice_date": notice_date.strftime("%Y-%m-%d"),
        "backup_date": formatted_date,
        "hide_after": hide_after.strftime("%Y-%m-%d"),
    }

    # Render template
    content = render_template(args.template, context)

    if args.dry_run:
        print(f"\n[DRY RUN] Would create {filepath} with content:")
        print("=" * 60)
        print(content)
        print("=" * 60)
    else:
        # Create output directory if it doesn't exist
        filepath.parent.mkdir(parents=True, exist_ok=True)

        # Write the file
        filepath.write_text(content)
        print(f"✓ Created {filepath}")

        # Set GitHub Actions output
        if "GITHUB_OUTPUT" in os.environ:
            with open(os.environ["GITHUB_OUTPUT"], "a") as f:
                f.write("created=true\n")
                f.write(f"filename={filepath}\n")
                f.write(f"backup_date={formatted_date}\n")


if __name__ == "__main__":
    main()
