# Bill Service

This application is a Flask-based REST API that handles CRUD operations for a hotel guest billing database. The data is stored in an SQLite database (bills.db), which is connected to a Docker volume to ensure persistent data storage.

## Functionality

The API offers the following features:

- **Get all bills** - Retrieves a list of all bills.

- **Get a bill by guest ID** - Retrieves a bill based on a guest's unique ID.

- **Get a bill by bill ID** - Retrieves a bill using the bill's unique ID.

- **Add a new bill** - Adds a new bill entry to the database.

- **Update bill status** - Updates the payment status of an existing bill.

- **Delete a bill by bill ID** - Deletes a bill based on its ID.


## Endpoints

### GET	/bills	
Returns a list of all bills.

```bash
GET /bills
```


### GET	/bills/guest/<guest_id>	
Retrieves a bill based on the guest's unique ID.

```bash
GET /bills/guest/<guest_id>
```


### GET /bills/<bill_id>
Retrieves a specific bill using its unique ID.

```bash
GET /bills/<bill_id>
```


### POST	/bills	
Adds a new bill to the database.

```bash
POST /bills
```


### PUT	/bills/<bill_id>	
Updates the payment status of an existing bill.

```bash
PUT /bills/<bill_id>
```


### DELETE	/bills/<bill_id>	
Deletes a bill based on its ID.

```bash
DELETE /bills/<bill_id>
```


## Installation


### Build and Run the Application

1. Build the Docker Image:
   ```bash
   docker build -t bill_service .
   ```

3. Run the Docker Container with a Volume Binding:
   ```bash
   docker run -it -p 5000:5000 -v bill_data:/app/data bill_service
   ```
