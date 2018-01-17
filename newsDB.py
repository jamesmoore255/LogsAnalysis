#!/urs/bin/env python

import psycopg2

print "running"

DBNAME = "news"


def popularArticles():
    try:
        db = psycopg2.connect(database=DBNAME)
        print "connected!"
        c = db.cursor()
        query = '''select articles.title as article, count(*)as num
        from articles, log
        where '/article/' || articles.slug = log.path
        group by articles.title
        order by num desc
        limit 3;'''
        c.execute(query)
        rows = c.fetchall()

        print "----Popular Articles----"
        for row in rows:
            print('{} -- {} views'.format(row[0], row[1]))

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        db.close()


def popularAuthors():
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        query = '''select authors.name, count (*) as num
        from authors, articles, log
        where authors.id = articles.author
        and articles.slug like substring(log.path from 10)
        group by authors.name
        order by num desc'''
        c.execute(query)
        rows = c.fetchall()

        print "----Popular Authors----"
        for row in rows:
            print('{} -- {} views'.format(row[0], row[1]))

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        db.close()


def errors():
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        query = '''select to_char(time, 'DD FMMonth YYYY') as date,
        (count(status) filter (where status like '404%'))
        * 100.0 / (count(status)) as errors
        from log group by date
        having errors (status) > 1.0;'''
        c.execute(query)
        rows = c.fetchall()

        print "----Errors Table----"
        for row in rows:
            print('{} -- {}%'.format(row[0], row[1]))

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        db.close()

if __name__ == '__main__':
    popularArticles()
    popularAuthors()
    errors()
