---
title: "History of the Statical Computing Facility"
---

(origin)=
## Origin of the Statistical Computing Facility

written by Leo Breiman, adapted by Rick Kawin in the 1990s

The Statistical Computing Facility (SCF) is an arm of the Statistics
Department, but with separate budget and personnel, and functions
independently of other University computing centers. Seventy percent of
its annual operating budget goes to salaries and benefits. Most of its
budget is provided by the University. The rest comes from grants and
other income sources. The staff consists of 4.0 FTEs who are systems
support and statistical software experts.

In 1981 Leo Breiman was appointed Directory of the Statistical
Laboratory. The Statastical Laboratory began by sharing computing
facilities with the Mathematics department and jointly operated a group
of VAX 11/750 computers (bach, mozart, brhams, and bizet). In January
1986 the Mathematics department moved its computer operations to Central
Campus Computing (IS&T) and the SCF was formed and became an independent
computing facility. The planning and work stretched over several years.

The first area developed was our graduate instructional program. We
started using 'S', a statistical language written at Bell Labs, and
became the first beta-test site for it. By the mid to late 1980's, many
of our graduate courses were making heavy use of computing, and almost
without exception our advanced degree students were knowledgeable
computer users.

In the mid 1980s, the decision was also made to integrate computing into
our undergraduate program. For this, hardware, software, and course
materials were required. The earliest hurdle was software: the 'S'
system was very CPU intensive and difficult for unskilled users.

In the early 1980's there was virtually no statistical software
available that ran under UNIX. A group in our department developed a
program called BLSS (Berkeley Interactive Statistical System) which we
used for undergraduate instruction. The advantages of BLSS were that it
ran efficiently and had a relatively simple user interface. We
approached the University in 1985 and asked for funds for BLSS
development, arguing that part of a university's function was to develop
good instructional tools. The University agreed and funded a three year
project. BLSS is now used in over 70 universities, and a book is
available (Abrahams and Rizzardi, 1988).

We also needed computing hardware capable of supporting 1500 student
users per semester. We decided that with good scheduling, this could be
done with 50 terminal stations driven by a SUN 4/280 server. All of the
faculty involved in this project had a strong belief that graphics were
essential. Since the only low cost graphics available in the UNIX
environment at that time were Tektronix compatible terminals, this was
the hardware selected.

Between the years 1985-1987, funds were obtained for hardware, partly
from the University and partly from donations. The Central Campus
Computing (IS&T) first transferred 21 Sun 3/50's (9 3/50's under loan
W00165 followed by 8 more 3/50's under loan W00196, and a final 4 3/50's
under loan W00661) to the facility between 1985-1986. Three rooms were
remodeled into terminal rooms. During the academic year 1986-87 and
summer of 1987, the department funded a project to develop instructional
materials for computer projects to serve as accompaniments to the
material being given in lectures and sections. The fall of 1987 was the
maiden voyage period.

At present, computing is integrated into most of the courses in the
undergraduate curriculum, from the most elementary to the most advanced,
with the result that there are about 3000 student computer accounts per
year provided by the Facility. We have learned that the use of computing
in instruction is as essential to the understanding of statistics as
laboratory experiments are in chemistry or physics.

Since 1987, experience has brought modifications in our use of computing
in the lower division instructional program. For instance, even the
simple command line structure of BLSS was difficult for many students.
They did not understand why the computer would complain about a
misplaced comma. The conclusion, after the first year, was that a
simpler interface was needed. In the summer of 1989, a menu driven
interface was constructed for our Tektronix compatible terminals.

This turned out to be time consuming. The graphics protocols of these
terminals were not designed to permit simple local programming of menus,
or of any of the other graphic interfaces and displays that have become
familiar in current technology. But going to this menu interface turned
out to be a big success in the lower division courses. Students were
able to focus more on the content of their projects rather than on the
frustrations of remembering and correctly typing the required command
lines.

It was also clear to us that introducing computing for the sake of
sitting students at computers so that they could rapidly calculate means
or standard deviations was a sterile exercise. The problem was how to
best use computers as an instructional tool.

Lower division students have had difficulties understanding
probabilistic concepts. The instructor can say as often as he/she likes
that in the long run, the frequency that this happens is 95 and the
statement has, with a similar frequency, very little impact on the
undergraduates listening. Or, the instructor can discuss the convergence
of the distribution of normalized sums of independent variables to the
normal distribution with as much simplicity as can be introduced, but
this is not a natural concept to the students. While they may memorize
it to disgorge on exams, it will remain an alien piece of information.

The Tektronix protocols do not support multiple window displays.
Programming simple graphic displays is time consuming, and interactive
communication between user and computer utilizing dynamic graphic
representations is impossible. Even though for years we could think (and
often did) of more effective graphic programs that would interact with
students and sharpen their intuitive understanding of probabilistic
concepts and data, these remained as notes for someday. Meanwhile we
were carefully watching the development of the X-Window technology.

Our thinking was that when this technology matured, it could give us the
graphic capabilities that are necessary for the further development of
our instructional programs. We had been testing a variety of X-Window
terminals starting in 1989, and seen their development reach the point
where their use will let us make a significant improvement in our
undergraduate instructional program.

The SCF, in 1990, received 16 Sun 1+'s (Model 4/65) as a donation from
Sun Microsystems and an additional 10 Sun 1+'s (Model 4/65) were
purchased as part of an NSF research grant (NSF-DMS90-05689). In 1991,
we applied to the Instrumentation and Laboratory Improvement Program of
the NSF for funds to purchase 50 X-Window terminals and a more powerful
Sun server to drive them. We were awarded funding and recieved the
X-terminals in Febuary of 1993 and the SPARC 2000 server in June of
1993. Due to problems with the operating system software, the equipment
was not made available for instructional use until the 1994 spring
semester.

The next step was a three year project to design and implement the
instructional projects.

(hardware-software)=
## Hardware and Software Platforms

written by Mark Abrahams, updated by Ryan Lovett

Computing in the Department may be divided into several eras, according
to the main type of computer equipment used. Each successive wave, or
generation, of equipment provided significant new abilities and allowed
successively more complex and capable software to be run. Each wave
built on the departmental knowledge and expertise acquired with the
preceding wave. Here are the main waves of equipment and the dates that
each arrived:

 - 1974: PDP-11/45
 - 1979: expanded PDP-11/45
 - 1982: VAX 750s
 - 1986: Sun3 Workstations
 - 1990: Sun SPARCstations
 - 1997: Sun Ultra workstations
 - 2003: amd64 compute servers
 - 2004: Sun Java workstations
 - 2005: Apple iMacs
 - 2010: Nvidia GPUs

The first Departmental computer was a PDP 11/45 obtained in 1974 jointly
by the Statistics, Mathematics, and CS Departments. Its early history is
described in the following section, [](#unix).
For the first few years the 11/45 had limited
capability in statistical computing. My understanding is that it was
used mainly for running locally-written BASIC programs and for learning
programming and computer software maintenance. Most serious statistical
computing, with datasets of any significant size, was done on the campus
computer center's mainframe (a CDC 6400).

In 1979, the abilities of the PDP 11/45 were expanded greatly with the
addition of two Ampex 80MB removable disk drives (the previous disk
storage was two RK05 diskpacks, which were about 3 or 4MB per pack).
Also (if I recall correctly) a hardware floating point unit was added
about that time and, shortly after, an Able memory controller which
allowed increased RAM. 7th Edition UNIX was installed in 1980. Two
reasonably reliable Fortran compilers were available, as was a C
compiler. The improvements in machine performance, system software, and
—most significantly—the 20-fold increase in disk space had marked
effects. Freestanding statistical programs could be written in Fortran
or C (or a mixture) and an interactive statistical program (ISP)
allowed, for the first time, easy to use interactive statistical
computing. The number of regular users in the department increased to a
dozen or more, and several classes made use of the software, especially
ISP.

In 1982, the Department acquired the first of what was ultimately three
VAX 750's. Though their cpu speed was not much more than the PDP 11/45,
they were 32-bit machines (as opposed the 16-bit PDP-11) with true
virtual memory, larger disks, and they ran 4BSD UNIX. This meant that
significantly larger programs could be run (using a 32-bit address space
instead of the 2 x 16-bit address space of the PDP 11). In particular,
the statistical system 'S' (which made significant demands on memory and
cpu) was installed and, in time, became heavily used by graduate
students. With 4BSD, the VAXes also provided much better networking
capabilities than did the PDP11. The VAXes and their associated
peripherals allowed, perhaps for the first time, everyone in the
department who wanted to find an available terminal almost whenever they
wished. The computer center mainframe (by now, an IBM) had more power
than the Department VAXes, but because the Departmental system became
increasing convenient to use, more and more people in the Department
began to choose it over the computer center. Thus the VAXes were the
beginning of serious 'Departmental computing' for statistical research.

In 1986, the Department acquired clusters of Sun3 workstations and
servers as part of a large University purchase. The Suns provided, for
the first time, large bit-mapped screens with graphical user interfaces.
They also provided NFS and the model of distributed computing power with
centralized disk servers we still use now. Each workstation had a
somewhat faster cpu than a VAX 750; more important, the Department soon
had over 20 Sun3 cpus compared to only 3 VAXes, and because they were
networked together and run as a single system, any user could access any
cpu. Total available cpu power thus increased by an order of magnitude;
and for the first time, a few large or long-running jobs would not
negatively impact other users because other cpus were unaffected. The
number and variety of software applications increased. By this point,
the departmental computing system was becoming more attractive as a
statistical computing environment than the computer center.

In 1990, the Department replaced most of its Sun3 Workstations with Sun
SPARCstation 1+'s. Though the software changes were evolutionary, the
cpu speed was between 5 and 10 times faster (depending on how it was
measured). Thus the size and complexity of application software could
increase correspondingly. By the mid 1990's, if not earlier, the
Department had far more statistical applications installed than did the
computer center.

In 1997, the Department replaced most of its SPARCstations with Sun
ULTRA-2 workstations. These gave another near-10-fold increase in cpu
power. They also came with color video displays, replacing the greyscale
displays of the SPARCstations (which had replaced the monochrome
displays of the Sun3's).

(unix)=
## How UNIX Came to UC Berkeley and the Department of Statistics

written by Mark Abrahams

(Excerpted and expanded from my dissertation, Design of BLSS Statistical
Software, Chapter 1, Section 5, Copyright (c) 1996 by D. Mark Abrahams)

In 1974, three departments—Mathematics, Statistics, and Computer Science—obtained a minicomputer for joint use. It was purchased with
funds left over from the NSF grant used to construct the (then) new
mathematical sciences tower, Evans Hall, which housed all three
departments. A PDP-11/45 was purchased for about \$120,000 and installed
in June 1974. It was selected and overseen by a committee composed of
Professors David Brillinger (the committee chair, of Statistics) Rene'
Devogelaere (of Mathematics), and Martin Graham (of Computer Science).
The committee considered several vendors, but Graham held firm for
DEC.[^1]

The Math/Stat/CS PDP-11/45 was installed in Room 450 Evans Hall, which
had been designed with air conditioning and a sunken machine-room floor
for the purpose of housing minicomputer equipment. From the first, the
new machine ran a DEC operating system, RSTS. However, a new,
little-known operating system was just then becoming available outside
the research laboratory where it was developed: UNIX from Bell Telephone
Laboratories. The PDP-11/45 logbook[^2] indicates that RSTS was first
booted on it on 3 June 1974, and UNIX on or before 6 June 1974.

The push to run UNIX came from Professor Robert Fabry of Computer
Science, who replaced Graham on the computer committee shortly after the
purchase. David Brillinger believes that the machine may have been the
first outside Bell Labs to run UNIX. The book by Salus[^3] suggests
otherwise—Salus says that UNIX was installed on some machines outside
Bell Labs by the end of 1973. However, Salus is wrong on some dates—in
particular, he recounts the Math/Stat/CS PDP-11/45 but with incorrect
dates. In any case, Room 450 was one of the first sites outside Bell
Labs to run UNIX. The then-current version was Fifth Edition, dated June
1974. The preface for its manual opened with the (now-famous) remark:

:::{blockquote}
The number of UNIX installations is now above 50, and many more are
expected.
:::

Ken Thompson of Bell Labs, one of main UNIX authors and a UC Berkeley
graduate, visited Computer Science in fall term 1974 and again in
1975-76, gave a number of talks on the then-new UNIX operating system,
and debugged UNIX on the 11/45.

Of course, the machine could run only one of the two operating systems
at a given time. The OS was changed easily enough: shut down one system,
swap the RK05 removable disk packs, boot the other system. Far more
vexing was the question of which OS would run when. CS used only UNIX
and wanted nothing to do with RSTS; Mathematics used only RSTS and
wanted nothing to do with UNIX. Statistics was in the middle, and
Brillinger often found himself mediating between the other two
departments. The question of which OS would run when was a subject of
contention for many years.

The first terminals were Teletype hardcopy units. Most were 'low-speed'
(Teletype models 33 and 35) which ran at 110 baud, but a few were
'high-speed' (Teletype model 37) which ran at 150 and 300 baud.

The Computer Science Division later purchased its own computers to run
UNIX full-time and withdrew from the joint agreement with Math and Stat.

Use of minicomputers spread across the campus. The campus Computer
Center Newsletter noted, in August 1976:

::: {blockquote}
There are now 44 DEC (Digital Equipment Corporation) machines on
campus that we know of, probably some that we don't know of, and more
arriving all the time.[^4]
:::

It is likely that only a minority of those 44 machines ran UNIX. But its
popularity spread, and the university computer center itself began to
purchase PDP-11/70's to run UNIX. The first was announced in December
1976:

::: {blockquote}
Hardware to provide UNIX service has been obtained with University
funds under the joint auspices of the CC \[Computer Center\] and the
Faculty Committee for Interactive Instruction on the UNIX 11/70. The
system has a principal mission of providing interactive support for
instruction in the social sciences. However, any excess capacity is to
be made available to the general campus computing community with
emphasis placed on developing diverse uses. ....

We have a ferocious problem with allocating the existing resources and
planning future hardware configurations. In order to prevent system
overload, the applications will be reviewed by the committee to decide
what users should have access to UNIX in the near future.[^5]
:::

A gradually increasing number of PDP-11's running UNIX were installed on
campus. By 1979, the computer center had five 11/70's, one of which was
devoted to the School of Business Administration. In addition to
Math/Stat and EECS, at least one other non-central unit—the Survey
Research Center—had its own.

About this time the Computer Science Division began a series of major
enhancements to UNIX which resulted in Berkeley UNIX. Fabry became one
of the principal investigators for the research projects which resulted
in these developments.

Computer Science began obtaining VAXes in 1978; the Computer Center
obtained its first VAX (an 11/780) in late 1980 and put it in general
service on 1 April 1981.[^6] Statistics obtained its first VAX, an
11/750, in March 1982. The push came from Professor Leo Breiman, who
wrote a successful ONR grant proposal in part for this purpose.

[^1]:  I am grateful to David Brillinger for supplying some of the early
       history here, and for making available to me his old computer
       committee notes from which I was able to derive more.
[^2]:  Which I rescued from the trash some years ago.
[^3]:  Peter H. Salus (1994), A Quarter Century of UNIX, Addison-Wesley.
       Page 137 gives a somewhat incorrect recounting of the Math/Stat/CS
       PDP-11/45.
[^4]:  Vance Vaughan (1976), in University of California, Berkeley,
       Computer Center Newsletter, Vol. XV, No. 8, 1976, p. 1.
[^5]:  Vance Vaughan (1976), in University of California, Berkeley,
       Computer Center Newsletter, Vol. XV, No. 12, 1976, p. 5.
[^6]:  Jerome Smith (1981), in University of California, Berkeley,
       Computing Services Newsletter, Vol. 4, No. 4, April 1981, p. 10.

## The Naming of Systems

Once upon a time, Stat (and Math) used the names of great composers (How
we got *those* is another story.). But Leo decided that with the Suns, we
would use names of characters from classic children's stories. His reason
was that he wanted something to express the excitment and wonder which go
along with learning and discovery, and he felt that the classic children's
story characters expressed it best. Leo chose the stories and the first
few names. Originally he chose three stories, which gave these names:

### The Wind in the Willows

- badger
- mole
- otter
- toad

### Winnie the Pooh

- eeyore
- heffal(ump)
- kanga
- piglet
- pooh
- rabbit
- roo
- tigger
- winnie
- wizzle
- wol
- woozle

### The Wizard of Oz

- (scare)crow
- dorothy
- lion
- glinda
- oz
- tinman
- toto
- witch
- wizard

### The Lord of the Rings

Later, Leo decided we should also use Tolkien names. That seems to have
been the most popular; also it's very practical because there are so
many Tolkien characters we'll never run out. So far we have:

- aragorn
- arwen
- balrog
- bilbo
- bombadil
- boromir
- denethor
- ea
- eomer
- eowyn
- fangorn
- faramir
- feanor
- frodo
- gandalf
- ghan
- gimli
- gollum
- gorbag
- grima
- legolas
- merry
- morgoth
- pippin
- radagast
- samwise
- saruman
- sauron
- shadowfax
- shagrat
- shelob
- smeagol
- springer
- strider
- treebeard
- ugluk

shagrat was also used for a while, but dropped because it turns out to
be an offensive vulgarity in the Australian language. (which is like
English, but different ☺︎)

### Harry Potter

When names became scarce, Ryan Lovett added characters from the Harry
Potter series.

- bellatrix
- dobby
- dumbledore
- ginny
- gryffindor
- hagrid
- harry
- hedwig
- hermione
- hufflepuff
- luna
- lupin
- malfoy
- quidditch
- ravenclaw
- ron
- sirius
- slytherin
- snape
- voldemort

The other names also have stories. They are (or oringally were) faculty
and staff workstations and named by their (original) main users. Some
reflect the national origins of their choosers.

antares  
: chosen by James Blakly because it's big and it's red and it's there.

arkle  
: chosen by Finbarr O'Sullivan; famous Irish racehorse.

bunyip  
: chosen by Jim Pitman. Bunyip Bluegum is a famous Australian children's
story character (note consistency with Leo's theme).

calvin  
: chosen by Alex Liu from the comic strip Calvin and Hobbes. (He also used
hobbes for awhile) (again note loose consistency with Leo's theme).

kestrel  
: chosen by Deb Nolan.

lorax and horton
: chosen by Dan Ackerman, after Dr. Seuss characters.

smiley  
: chosen by Andrew Gelman.

springer  
: chosen by Steve Peters in honor of his springer spaniel, Benjamin.

vif  
: chosen by Kjell Doksum. Famous Norwegian soccer team (what else would
you expect him to choose?)

wanjina  
: chosen by Steve Evans (name used for an Australian shaman).

zardoz  
: chosen by Dave Donoho, after the science fiction movie of the same name.
