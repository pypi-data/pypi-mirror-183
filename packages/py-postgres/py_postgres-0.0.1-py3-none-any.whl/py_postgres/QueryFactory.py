def build_select_query(select_from, select_select, select_where, select_left_join, select_order_by,
                       select_order_direction):
    query = ''
    if type(select_select) == str:
        query = f'SELECT {select_select} FROM {select_from}'
    elif type(select_select) == list:
        selects = ''
        for i in range(0, len(select_select)):
            if i == len(select_select) - 1:
                selects += f'{select_select[i]}'
            else:
                selects += f'{select_select[i]}, '
        query = f'SELECT {selects} FROM {select_from}'
    if select_left_join is not None:
        if len(select_left_join) != 3:
            raise IndexError('select left join has to have 3 items (3 strings or 3 lists)')
        else:
            if type(select_left_join[0]) == str and type(select_left_join[1]) == str \
                    and type(select_left_join[2]) == str:
                query += f' LEFT JOIN {select_left_join[0]} ON {select_left_join[1]} = {select_left_join[2]}'
            elif type(select_left_join[0]) == list and type(select_left_join[1]) == list \
                    and type(select_left_join[2]) == list:
                if len(select_left_join[0]) == len(select_left_join[1]) == len(select_left_join[2]):
                    join_tables = select_left_join[0]
                    on_1 = select_left_join[1]
                    on_2 = select_left_join[2]
                    joins = ''
                    for i in range(0, len(join_tables)):
                        joins += f' LEFT JOIN {join_tables[i]} ON {on_1[i]} = {on_2[i]}'

                    query += joins
                else:
                    raise IndexError('the 3 lists have not the same length')
            else:
                raise TypeError('The 3 elements in this parameter have to be either (string, string, string) or ('
                                'list, list, list)')
    if select_where is not None:
        query += f' WHERE {select_where}'
    if select_order_by is not None:
        if type(select_order_by) == str:
            query += f' ORDER BY {select_order_by}'
        elif type(select_order_by) == list:
            orders = ''
            for i in range(0, len(select_order_by)):
                if i == len(select_order_by) - 1:
                    orders += f'{select_order_by[i]}'
                else:
                    orders += f'{select_order_by[i]}, '

            query += f' ORDER BY {orders}'
    if select_order_direction is not None:
        if select_order_direction in ['ASC', 'DESC']:
            query += f' {select_order_direction}'
        else:
            raise ValueError('select order direction has to be ASC or DESC')

    return query


def build_insert_query(insert_into, columns, values):
    if type(insert_into) == str:
        query = f'INSERT INTO {insert_into}'
    else:
        raise TypeError('insert into has to be the table name as string')

    if type(columns) == tuple and len(columns) > 0:
        columns_string = '('
        format_string = '('
        for i in range(0, len(columns)):
            if i == len(columns) - 1:
                columns_string += f'{columns[i]})'
                format_string += '%s)'
            else:
                columns_string += f'{columns[i]}, '
                format_string += '%s, '
        query += f' {columns_string} VALUES {format_string}'
    else:
        raise TypeError('values has to be a tuple with len > 0')

    if type(values) == list:
        for value_line in values:
            if type(value_line) == tuple:
                if len(value_line) == len(columns):
                    continue
                else:
                    raise IndexError('every tuple in the value list has to be same length as the columns tuple')
            else:
                raise TypeError('every line of values has to be a tuple')
    else:
        raise TypeError('values has to be a list of tuples. can contain one tuple or more')

    return query
