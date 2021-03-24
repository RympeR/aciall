from .psycopg_sql import *


class UserFilter:

    def where_add(self, query):
        if 'where' not in query:
            query += '\nwhere'
        return query

    # TODO-- UPDATE METHOD
    def add_in_case(self, request, query, param_name, field_name):
        if request.query_params.get(param_name, None) not in ('empty', '', None):
            query = self.where_add(query)
            param = request.query_params[param_name]
            if query.split('\n')[-1].strip() != 'where':
                for value in param:
                    query += f"\nand {field_name} in '%'"
            else:
                for value in param:
                    query += f"\n{field_name} like '%{param}%'"
        return query

    def add_and_case(self, request, query, param_name, field_name, str_=True):
        if request.query_params.get(param_name, None) not in ('empty', '', None):
            query = self.where_add(query)
            param = request.query_params[param_name]
            if query.split('\n')[-1].strip() != 'where':
                if str_:
                    query += f"\nand {field_name} like '%{param}%'"
                else:
                    query += f"\nand {field_name}= {param}"
            else:
                if str_:
                    query += f"\n{field_name} like '%{param}%'"
                else:
                    query += f"\n{field_name}= {param}"
        
        return query

    def add_between_case(self, request, query, param_name, param_end_name, field_name, str_=True, or_=False):
        if request.query_params.get(param_name, None) not in ('empty', '', None):
            query = self.where_add(query)
            param = request.query_params[param_name]
            param_end = request.query_params.get(param_end_name, None)
            if query.split('\n')[-1].strip() != 'where':
                if not or_:
                    if str_:
                        if param_end:
                            query += f"\nand {field_name} between '{param}' and '{param_end}'"
                        else:
                            query += f"\nand {field_name} >= '{param}'"
                    else:
                        if param_end:
                            query += f"\nand {field_name} between {param} and {param_end}"
                        else:
                            query += f"\nand {field_name} >= {param}"
                else:
                    if str_:
                        if param_end:
                            query += f"\nor {field_name} between '{param}' and '{param_end}'"
                        else:
                            query += f"\nor {field_name} >= '{param}'"
                    else:
                        if param_end:
                            query += f"\nor {field_name} between {param} and {param_end}"
                        else:
                            query += f"\nor {field_name} >= {param}"
            else:
                if str_:
                    if param_end:
                        query += f"\n {field_name} between '{param}' and '{param_end}'"
                    else:
                        query += f"\n {field_name} >= '{param}'"
                else:
                    if param_end:
                        query += f"\n {field_name} between {param} and {param_end}"
                    else:
                        query += f"\n {field_name} >= {param}"
        return query

    def get_users(self, request, login, password):
        base_query = '''
            select id, phone,  last_name, first_name, avatar from users_user
        '''
        try:
            query = base_query
            query = self.add_and_case(
                request, query, 'first_name', 'users_user.first_name')
            query = self.add_and_case(
                request, query,  'last_name', 'users_user.last_name')
            query = self.add_and_case(
                request, query, 'phone', 'users_user.phone')
            query += ';'
            print(query)
            result = execute_select_query(login, password, query)

        except Exception as e:
            print(e)
            print('failed')
            query = base_query + ';'
            result = execute_select_query(login, password, query)
        return result