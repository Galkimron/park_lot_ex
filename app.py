from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

parking_lot = {}


@app.route('/entry', methods=['POST'])
def entry():
    plate = request.args.get('plate')
    parking_lot_id = request.args.get('parkingLot')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    ticket_id = len(parking_lot) + 1
    parking_lot[ticket_id] = {'plate': plate, 'entry_time': timestamp, 'parking_lot_id': parking_lot_id}

    return jsonify({'ticket_id': ticket_id})





@app.route('/exit', methods=['POST'])
def exit():
    ticket_id = int(request.args.get('ticketId'))
    ticket = parking_lot.get(ticket_id)

    if ticket:
        entry_time = datetime.datetime.strptime(ticket['entry_time'], '%Y-%m-%d %H:%M:%S')
        exit_time = datetime.datetime.now()
        parked_time = exit_time - entry_time
        charge = round(parked_time.total_seconds() / 3600 * 10, 2)

        response = {
            'plate': ticket['plate'],
            'parked_time': str(parked_time),
            'parking_lot_id': ticket['parking_lot_id'],
            'charge': charge
        }

        del parking_lot[ticket_id]

        return jsonify(response)
    else:
        return jsonify({'error': 'Invalid ticketId'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
