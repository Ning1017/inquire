from py2neo import Graph
from . import inquire
from flask import render_template
from .. import CONFIG_MAP

# CONFIG = current_app.config
# graph = Graph(CONFIG_MAP['NEO4J_BOLT'],
#               username=CONFIG_MAP['NEO4J_USER'],
#               password=CONFIG_MAP['NEO4J_PASSWORD'])

graph = Graph('http://10.3.10.205:7474',
              username='neo4j',
              password='neo4j123')

@inquire.route('/', methods=['GET', 'POST'])
def index():
    # 查找对应节点
    # matcher = NodeMatcher(graph)
    # node = matcher.match('City', id = 'dist154').first()
    # print(node)

    graph = Graph('http://10.3.10.205:7474',
                  username='neo4j',
                  password='neo4j123')

    # 通过数据库语言进行查找
    list = graph.run("MATCH (n:Expert) WHERE n.gender = '1' RETURN n.name limit 5").data()
    list1 = graph.run("match (n1:Expert{gender:'2'}) return n1.name limit 5").data()
    print(list)
    print(list1)

    return render_template('inquire.html')
    # 找某个节点相邻的点
    # for word in list:
    #     result_list = graph.run('MATCH p=(na:Expert)-[r:workAt]->(nb:Company) where nb.city=371200 RETURN na').data()
    # print(result_list)
    # result_list1=str(result_list).encode('utf-8').decode('unicode_escape')
    # print(result_list1)