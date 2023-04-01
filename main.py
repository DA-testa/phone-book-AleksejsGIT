# python3
# Aleksejs Šepeļevs, 3.grupa, 221RDB494

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        
        if len(query[1])<=7:
            if self.type == 'add':
                self.name = query[2]
                if len(query[2])>15:
                    print ("wrong")

def read_queries():
    n = int(input())
    if n<1 or n>999999:
        print ("wrong")
    else:
        return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # saglabāt kā dictionary nevis list
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur.query.name

        elif cur_query.type == 'del':
            contacts.pop(cur.query.number, None)
        else:
            response = contacts.get(cur_query.number, 'not found')
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

