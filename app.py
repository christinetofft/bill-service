"""Bill Service"""

import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)



#Get all bills
@app.route('/bills', methods=['GET'])
def get_bills():
    with sqlite3.connect("/app/data/bills.db") as conn: 
        cur = conn.cursor()
        bills = cur.execute(""" SELECT * FROM bills """)
        rows = cur.fetchall()
        return rows
        

#Create new bill
@app.route('/bills', methods=['POST'])
def add_bill():
    data = request.json
    guest_id = data.get("guestId")
    bill_id = data.get("billId")
    item = data.get("item")
    price = data.get("price")

    with sqlite3.connect("/app/data/bills.db") as conn:
        cur = conn.cursor()
        cur.execute(""" INSERT INTO bills 
                    (
                    guest_id, 
                    item, 
                    price, 
                    paid_status
                    )
                    VALUES (?,?,?,?)
                     """,(guest_id, item, price, False))
        conn.commit()

    return "success"


#Get specific bill by guest ID
@app.route('/bills/guest/<int:guest_id>', methods=['GET'])
def get_bill_guest_id(guest_id):
    with sqlite3.connect("/app/data/bills.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM bills WHERE guest_id = ?", (guest_id,))
        row = cur.fetchone()

        if row:
            #If a bill is found, return it to JSON:
            return jsonify({
                "guest_id": row[0],
                "item": row[1],
                "price": row[2],
                "paid_status": row[3],
                "bill_id": row[4]

            })
        else:
            #Return an error if bill is not found:
            return "error: bill not found", 404
    

#Get specific bill by bill ID
@app.route('/bills/<int:bill_id>', methods=['GET'])
def get_bill_bill_id(bill_id):
    with sqlite3.connect("/app/data/bills.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM bills WHERE bill_id = ?", (bill_id,))
        row = cur.fetchone()

        if row:
            #If a bill is found, return it to JSON:
            return jsonify({
                "guest_id": row[0],
                "item": row[1],
                "price": row[2],
                "paid_status": row[3],
                "bill_id": row[4]
            })
        else:
            #Return an error if bill is not found:
            return "error: Bill not found", 404
    

#Update bill by bill ID
@app.route('/bills/<int:bill_id>', methods=['PUT'])
def update_bill(bill_id):
    data = request.json
    paid_status = data.get("paid_status", False)

    with sqlite3.connect("/app/data/bills.db") as conn:
        cur = conn.cursor()
        cur.execute("UPDATE bills SET paid_status = ? WHERE bill_id = ?", (paid_status, bill_id))
        conn.commit()

        if cur.rowcount == 0:
            return "error: Bill not found", 404
        return "Bill updated successfully", 200


#Delete bill by bill ID
@app.route('/bills/<int:bill_id>', methods=['DELETE'])
def delete_bill(bill_id):
    with sqlite3.connect("/app/data/bills.db") as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM bills WHERE bill_id = ?", (bill_id,))
        conn.commit()

        if cur.rowcount == 0:
            return jsonify({"error": "Bill not found"}), 404
        return jsonify({"message": "Bill deleted successfully"}), 200

#Send all data
@app.route('/bills/data', methods=["GET"])
def get_bills_data():
    with sqlite3.connect('/app/data/bills.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM bills")
        data = cur.fetchall()

        #Check the response
        if not data:
            #response is empty
            return "There was an error trying to retrieve all bills!", 400
        return data


app.run(debug=True, host="0.0.0.0")
