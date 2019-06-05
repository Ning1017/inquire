from py2neo import Graph, NodeMatcher
from . import inquire
from flask import render_template
from .. import CONFIG_MAP

# CONFIG = current_app.config
graph = Graph(CONFIG_MAP['NEO4J_BOLT'],
              username=CONFIG_MAP['NEO4J_USER'],
              password=CONFIG_MAP['NEO4J_PASSWORD'])

@inquire.route('/', methods=['GET', 'POST'])
def index():

    # graph = Graph('http://10.3.10.205:7474',
    #               username='neo4j',
    #               password='neo4j123')

    # 查找对应节点
    matcher = NodeMatcher(graph)
    node = matcher.match('City', id = 'dist154').first()
    print(node)


    # 通过数据库语言进行查找
    test = 123
    list1 = graph.run("MATCH (n:Expert) WHERE n.gender = '1' RETURN n.name limit 5").data()
    list2 = graph.run("match (n1:Expert{gender:'2'}) return n1.name limit 5").data()

    return render_template('inquire.html',
                           test = test, list1 = list1, list2 = list2)
    # 找某个节点相邻的点
    for word in list:
        result_list = graph.run('MATCH p=(na:Expert)-[r:workAt]->(nb:Company) where nb.city=371200 RETURN na').data()
    print(result_list)
    result_list1=str(result_list).encode('utf-8').decode('unicode_escape')
    print(result_list1)

    return render_template('inquire.html',
                           test=test, node = node, list1=list1, list2=list2,
                           list3 = result_list, list4 = result_list1)