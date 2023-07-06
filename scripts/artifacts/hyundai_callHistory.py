import csv
import os
import sqlite3

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, logdevinfo, is_platform_windows, open_sqlite_db_readonly

#Compatability Data
vehicles = ['Hyundai Sonata']
platforms = ['Carplay']

def get_callHistory(files_found, report_folder, seeker, wrap_text):
    data_list = []
    for file_found in files_found:
        db = open_sqlite_db_readonly(file_found)
        cursor = db.cursor()
        

        cursor.execute("SELECT _id from bluetooth_callhistory")
        ids = cursor.fetchall()

        cursor.execute("SELECT given_name from bluetooth_callhistory")
        givens = cursor.fetchall()

        cursor.execute("SELECT family_name from bluetooth_callhistory")
        familys = cursor.fetchall()

        cursor.execute("SELECT phone_number from bluetooth_callhistory")
        phone_numbers = cursor.fetchall()

        cursor.execute("SELECT calltype from bluetooth_callhistory")
        callTypes = cursor.fetchall()


        cursor.execute("SELECT date from bluetooth_callhistory")
        dates = cursor.fetchall()

        cursor.execute("SELECT date_sort from bluetooth_callhistory")
        date_sorts = cursor.fetchall()

        cursor.execute("SELECT duration from bluetooth_callhistory")
        durations = cursor.fetchall()

        cursor.execute("SELECT numberType from bluetooth_callhistory")
        numberTypes = cursor.fetchall()
        i = 0
        for id in ids:
            id.replace("(", "")
            id.replace(")", "")
            id.replace(",", "")
            id.replace("'", "")
        for given in givens:
            given.replace("(", "")
            given.replace(")", "")
            given.replace(",", "")
            given.replace("'", "")
        for family in familys:
            family.replace("(", "")
            family.replace(")", "")
            family.replace(",", "")
            family.replace("'", "")
        for phone_number in phone_numbers:
            phone_number.replace("(", "")
            phone_number.replace(")", "")
            phone_number.replace(",", "")
            phone_number.replace("'", "")
        for callType in callTypes:
            callType.replace("(", "")
            callType.replace(")", "")
            callType.replace(",", "")
            callType.replace("'", "")
        for date in dates:
            date.replace("(", "")
            date.replace(")", "")
            date.replace(",", "")
            date.replace("'", "")
        for date_sort in date_sorts:
            date_sort.replace("(", "")
            date_sort.replace(")", "")
            date_sort.replace(",", "")
            date_sort.replace("'", "")
        for duration in durations:
            duration.replace("(", "")
            duration.replace(")", "")
            duration.replace(",", "")
            duration.replace("'", "")
        for numberType in numberTypes:
            numberType.replace("(", "")
            numberType.replace(")", "")
            numberType.replace(",", "")
            numberType.replace("'", "")

            j += 1

    #append array for each column to data_list, push data_list to report
        for id in ids:
            data_list.append((ids[i], givens[i], familys[i], phone_numbers[i], callTypes[i], dates[i], date_sorts[i], durations[i], numberTypes[i]))
            i += 1
    if len(data_list) > 0:
        report = ArtifactHtmlReport('Call History')
        report.start_artifact_report(report_folder, f'Call History')
        report.add_script()
        data_headers = ('id','given_name', 'family_name', 'phone_number', 'calltype', 'date', 'date_sort', 'duration', 'numberType')
        report.write_artifact_data_table(data_headers, data_list, file_found)
        report.end_artifact_report()
        tsvname = f'Call History'
        tsv(report_folder, data_headers, data_list, tsvname)
    else:
        logfunc(f'No Call History found')


__artifacts__ = {
    "call history": (
        "call history",
        ('*/bluetooth/DB_BMS/CH_*.db'),
        get_callHistory),
}