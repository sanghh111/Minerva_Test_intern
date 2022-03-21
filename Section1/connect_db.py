import sqlite3 

def connect_db(dbfile) :
    
    #con và cur lần lượt là connect và cursor trong dbfile
    con =  sqlite3.connect(dbfile)
    cur =  con.cursor()

    return con,cur


def check_absent_date_gt_3():

    # query that selects student_id and number of absent dates for each user who has more than 3 absent dates. Check-in dates are distinct    
    querry = '''
        select student_id , count() as "absent dates"
        From attendance as a1
        GROUP BY(student_id)
        Having count(absent_flag) > 3
    '''
    
    try :
        #return 1 list reuslt
        result = cur.execute(querry).fetchall()
        return result
    except Exception as e:
        #return Error
        return(e)
    

con,cur = connect_db('Section1.db')