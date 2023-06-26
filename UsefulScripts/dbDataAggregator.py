import mysql.connector
import logging
import pandas as pd

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_connection_to_db():
    try:
        cnx = mysql.connector.connect(user="all_restricted_ro",
                                      password="ahFahH2wui4YahH8",
                                      host="fsuite-db-ops-flock-com-1.cyy5hdjwfoo4.us-east-1.rds.amazonaws.com",
                                      database="mailbll")
        return cnx
    except mysql.connector.Error as err:
        logger.error("Failed to connect to DB")
        logger.exception(err)


def get_data(cnx, domain_id):
    cursor = cnx.cursor()
    query = (
        "select d.domain_name, u.customer_id, h.config->'$.apiConfig.host' as host from domains d INNER JOIN user_profile as u on d.user_id = u.id INNER JOIN hosting_servers h on d.hosting_server_id = h.id where d.id = {}".format(
            domain_id))
    cursor.execute(query)
    for (domain_name, customer_id, host) in cursor:
        return domain_name, customer_id, host


def main():
    # Connect to DB
    cnx = get_connection_to_db()

    # Then open CSV
    with pd.read_excel('/Users/anurag.sh/workspace/SQLDump/temp/HostgatorSetupFlowChecks.xlsx', "Sheet5") as file:
        # Then for each orderId fetch userId and HostingServer

        for index, row in file.iterrows():
            # print(index, int(row['order_id']))
            domain_name, customer_id, host = get_data(cnx, int(row['order_id']))
            # print(int(row['order_id']), domain_name, customer_id, host)
            if host is None:
                host = ''
            print('| {id:8} | {domain_name:35} | {customer_id:20} | {host:30}'.format(id=int(row['order_id']),
                                                                                      domain_name=domain_name,
                                                                                      customer_id=customer_id,
                                                                                      host=host))


if __name__ == '__main__':
    main()
