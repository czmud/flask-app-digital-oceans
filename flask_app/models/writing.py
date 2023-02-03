from flask_app.config.mysqlconnection import connectToMySQL

class Writing:
    def __init__( self, data ):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.content = data['content']

    @classmethod
    def save( cls, data ):
        query_string = "INSERT INTO creations ( title, description, writing ) \
            VALUES (%(title)s, %(description)s, %(content)s);"
        return connectToMySQL().query_db(query_string, data)

    @classmethod
    def query_db( cls ):
        # query_string = "SELECT TABLE_NAME FROM information_schema.tables WHERE table_schema='website';"
        query_string = "SELECT * FROM creatures WHERE id > 0;"

        return connectToMySQL().query_db(query_string)
    
    @classmethod
    def query_db_2( cls ):
        # query_string = "SELECT TABLE_NAME FROM information_schema.tables WHERE table_schema='website';"
        query_string = "SELECT * FROM writings WHERE id > 0;"

        return connectToMySQL().query_db(query_string)