import psycopg2

def load_to_redshift():

    conn = psycopg2.connect(
        dbname="dev",
        user="username",
        password="password",
        host="your-redshift-endpoint",
        port="5439"
    )

    cursor = conn.cursor()

    query = """
    COPY cricket_matches
    FROM 's3://your-bucket-name/'
    IAM_ROLE 'your-iam-role'
    FORMAT AS JSON 'auto';
    """

    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

    print("Loaded into Redshift")
