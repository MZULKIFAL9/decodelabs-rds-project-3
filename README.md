# RDS MySQL Intern Project
This project connects to an AWS RDS MySQL database using Python, 
creates an Interns table, inserts records, and tests constraints.

## How to run
1. Add your own .env file (see .env.example)
2. Install: pip install mysql-connector-python python-dotenv
3. Run: python main.py

## Security Notes
This RDS instance is configured as publicly accessible with the security 
group inbound rule restricted to a single trusted IP address on port 3306. 
For a production-grade setup, this would ideally be placed in a private 
subnet accessed only via a bastion host or VPN, but for this project's 
scope, IP-restricted public access provides sufficient security while 
allowing straightforward local development and testing.