---
title: Working with SQLite
---
This page has some information on using databases, in particular SQLite,
a flexible and straightforward database management system. With SQLite
you can create and manipulate databases locally on your own machine.
Note that if you need a more powerful client-server database management
system, such as postgreSQL, please [contact
us](mailto:consult@stat.berkeley.edu). SQLite is available on all of the
SCF Linux machines.

You can work with SQLite databases directly using the SQLite command
line tool, or via Python or R. We'll demonstrate a little bit of
functionality in all three. The example database we'll use is the
Current Index to Statistics (CIS), which is available on the SCF system
as an SQLite database at `/accounts/web/public/scf/cis.db`.

## The SQLite command line tool

To open a database (the same command will create a new database if one
of the given name doesn't exist) from the command line in UNIX:

:::{code} shell
sqlite3 /account/web/public/scf/cis.db
:::

This opens up the command-line tool. Here are some example operations to
find the tables in the database, get metadata on the tables and then do
some basic queries.

:::{code} sql
.tables
select * from sqlite_master;
select * from authors where name like 'Breiman%';
select * from authorships where author_id="532" or author_id="1141";
select * from articles where id_title="251483";
.exit
:::

Here's how you could do the same thing using a view (a virtual table):

:::{code} sql
create view fullAuthorInfo as select * from authors join authorships on authorships.author_id = authors.id;
create view fullArticleInfo as select * from articles join fullAuthorInfo on
   articles.id_title=fullAuthorInfo.id_title;
select * from fullArticleInfo where name like 'Breiman%';
:::

To create a table, we start the command line tool with the name we'd
like for the database file:

:::{code} shell-session
$ sqlite3 test.db
:::

:::{code} sql
create table mytable(id integer primary key, value text);
insert into mytable(id, value) values(1, 'Michael');
insert into mytable(id, value) values(2, 'Jenny');
insert into mytable(value) values('Francis');
select * from mytable;
.exit
:::

## Accessing a database from Python

Using the command-line tool is fine, but you probably want to use a
database to store data for use in analyses. For this, accessing the
database from Python or R is more useful.

The following script walks through the tables (necessary since the
authorship info is not directly available in the 'articles' table) to
find the articles by Leo Breiman.

:::{code} python
import sqlite3

db = sqlite3.connect("/account/web/public/scf/cis.db")
c = db.cursor()

a_ids = c.execute("select id from authors where name like 'Breiman%'").fetchall()
a_ids = [val[0] for val in a_ids]
a_ids

## [532, 1141]

t_ids = c.execute("select id_title from authorships where author_id in (" + ",".join("?" * len(a_ids)) +
  ")", a_ids).fetchall()
t_ids = [val[0] for val in t_ids]
t_ids

## [593, 1062, 1087, 1089, 1440, 2156, 2580, 2742, 3815, 5797, 6070, 12099, 23041, 27047, 31470, 31746,
## 35905, 41249, 62295, 64763, 75194, 80303, 80307, 82212, 82524, 106148, 109824, 110751, 111842, 123322, 
## 128020, 135085, 135089, 139595, 139596, 139712, 142755, 146230, 147372, 161725, 161777, 161785, 162277, 
## 170853, 173088, 186518, 187886, 192255, 192259, 207937, 212560, 229357, 229362, 242908, 251483]

breiman = c.execute("select * from articles where id_title in (" + ",".join("?" * len(t_ids)) + ")", t_ids).fetchall()
titles = [record[4] for record in breiman]

for title in titles:
    print(title)

## The individual ergodic theorem of information theory (Corr: V31 p809-810)
## The capacities of certain channel classes under random coding
## On the completeness of order statistics
## The strong law of large numbers for a class of Markov chains
## ...

c.close()
:::

## Accessing a database from R

And here is analogous code in R.

:::{code} r
library(RSQLite)

## Loading required package: DBI

db <- dbConnect(SQLite(), dbname = "/account/web/public/scf/cis.db")
dbListTables(db)

##  [1] "articles"              "authors"              
##  [3] "authorships"           "books"                
##  [5] "contacts"              "delayed_jobs"         
##  [7] "host_ips"              "host_names"           
##  [9] "isbns"                 "issns"                
## [11] "issues"                "journals"             
## [13] "rails_admin_histories" "tag_relations"        
## [15] "taggings"              "tags"                 
## [17] "users"                 "volumes"

dbListFields(db, "articles")

##  [1] "id"         "type"       "id_entity"  "id_title"   "title"     
##  [6] "year"       "volume"     "number"     "page_start" "page_end"  
## [11] "url"        "journal"    "journal_id" "volume_id"  "issue_id"  
## [16] "zmath"

a_ids <- dbGetQuery(db, "select id from authors where name like 'Breiman%'")
a_ids

##     id
## 1  532
## 2 1141

a_ids <- as.list(unlist(a_ids))
t_ids <- dbGetQuery(db, paste("select id_title from authorships where author_id in (", 
    paste(rep("?", length(a_ids)), collapse = ","), ")"), a_ids)
t_ids$id_title[1:5]

## [1]  593 1062 1087 1089 1440

dbDisconnect(db)
:::
