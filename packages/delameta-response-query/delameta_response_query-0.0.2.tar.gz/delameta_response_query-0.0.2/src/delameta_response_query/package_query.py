__all__ = [
    "pg_query_select"
]

class QueryData:
    def __init__(self, type_database):
        self.__modulename__ = "QueryData"
        self.__tipedatabase__ = type_database

    def normal_query_select(self, cursor, table_name:str, declare_column:list = None, alias_column:list = None 
                            , where_column:list = None, where_value:list = None, limit:int = None, offset:int = None, grouping_column:list = None
                            , ordering_column:str = None, ordering:str = "asc", like_column:list = None, or_column:list = None
                            , or_value:list = None, lowercase_column:list = None):
        """Query select postgresql
        cursor merupakan sebuah fungsi yang memiliki koneksi ke database
        table_name = nama table
        declare_column = nama kolom yang akan digunakan bisa juga digunakan seperti perintah sum(nama_kolom) dengan mengisi alias_column sebegai as 
        alias_column = alias dari declare_column
        where_column = kolom yang akan dicari
        where_value = isi dari kolom yang akan dicari
        limit = limit sebuah query
        offset = offset query
        grouping_column = group
        ordering_column = kolom yang akan di order
        ordering = tipe order
        like_column = column yang akan digunakan like
        or_column = column yang akan menggunakan or bukan and
        or_value = isi dari or_column
        lowercase_column = column yang akan menggunakan lowercase
        """
        if alias_column:
            if len(declare_column) != len(alias_column):
                raise ValueError("Jika alia_column ada, maka isi alias_column dan declare_column harus nama panjangnya")
        
        if len(where_column) != len(where_value):
                raise ValueError("Jumlah where_column dan where_value tidak sama")

        if alias_column and not grouping_column:
            raise ValueError("Jika menggunakan alias_column maka harus menggunakan grouping_column sesuai nama yang ada didalam alias_column")

        if or_column:
            if len(or_column) != len(or_value):
                raise ValueError("Jumlah or_column dan or_value tidak sama")

        __datavalue = []
        __sqltext = f"select "
        if not declare_column:
            __sqltext += " * "
        else:
            for idx, data_column in enumerate(declare_column):
                __sqltext += f"{data_column}"
                if alias_column:
                    __sqltext += f" as {alias_column[idx]}"
                if idx + 1 != len(declare_column):
                    __sqltext += ","
        __sqltext += f" from {table_name} "
        if where_column or or_column:
            __sqltext += " where "

        if where_column:
            for idx, data_where in enumerate(where_column):
                __lower_front = ""
                __lower_back = ""
                if str(data_where).lower() in list(map(lambda x: str(x).lower(), lowercase_column)):
                    __lower_front = "lower("
                    __lower_back = ")"
                if idx == 0:
                    if str(data_where).lower() in list(map(lambda x: str(x).lower(), like_column)):
                        __sqltext += f"{__lower_front}{data_where}{__lower_back} like {__lower_front}%s{__lower_back} "
                        __datavalue.append(f"%{where_value[idx]}%")
                    else:
                        __sqltext += f"{__lower_front}{data_where}{__lower_back} = {__lower_front}%s{__lower_back} "
                        __datavalue.append(where_value)
                else:
                    __sqltext += f" and {__lower_front}{data_where}{__lower_back} = {__lower_front}%s{__lower_back} "

        if or_column:
            __sqltext += " ( "
            for idx, data_or in enumerate(or_column):
                __lower_front = ""
                __lower_back = ""
                if str(data_or).lower() in list(map(lambda x: str(x).lower(), lowercase_column)):
                    __lower_front = "lower("
                    __lower_back = ")"
                
                if idx == 0 and not where_column:
                    if str(data_or).lower() in list(map(lambda x: str(x).lower(), like_column)):
                        __sqltext += f"{__lower_front}{data_or}{__lower_back} like {__lower_front}%s{__lower_back} "
                        __datavalue.append(f"%{or_value[idx]}%")
                    else:
                        __sqltext += f"{__lower_front}{data_or}{__lower_back} = {__lower_front}%s{__lower_back} "
                        __datavalue.append(or_value)
                else:
                    __sqltext += f" or {__lower_front}{data_or}{__lower_back} = {__lower_front}%s{__lower_back} "
            __sqltext += " ) "

        if grouping_column:
            __sqltext += " group by "
            for idx, data_group in enumerate(grouping_column):
                __sqltext += f" {data_group}"
                if idx + 1 != len(grouping_column):
                    __sqltext += ","

        if ordering_column:
            __sqltext += f" order by {ordering_column} {ordering}"

        if limit:
            __sqltext += f" limit %s"
            __datavalue.append(limit)
        
        if offset and limit:
            __sqltext += f" offset(%s*%s)"
            __datavalue.extend([offset, limit])
        __data = None
        
        with cursor() as query:
            try:
                query.execute(__sqltext, tuple(__datavalue))
                if limit == 1:
                    __data = query.fetchone()
                else:
                    __data = query.fetchall()

            except Exception as e:
                raise ValueError(e)

        return __data

                    
_pg_module = QueryData(type_database = "postgresql")
pg_query_select = _pg_module.normal_query_select
