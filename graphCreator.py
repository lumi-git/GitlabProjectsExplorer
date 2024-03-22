from sys import argv
import json

config = {
    
}

class ArgParser : 

    def __init__(self) -> None:
        self.entryDict = {}
    
    def argParsing(self):
        params = argv[1:]
        self.entryDict = self.createEntryDict(params)

    def createEntryDict(self, params):
        ret_dict = {}
        for i in range(0,int(len(params)-1),2):
            ret_dict[params[i]] = params[i+1]
        return ret_dict

    def parse(self): 
        self.argParsing()


def getDictAt(path:list,graph:dict) -> dict:
    print(graph)
    if len(path) == 0:
        return graph
    else: 
        getDictAt(path[1:],graph[path[0]])


def createMermaidDefFor(item,info="group"):
    """
    Crée une définition pour un élément du graphe Mermaid.
    """
    return f'class {item}{{{info}}}'

def createMermaidRelationFor(item1, item2):
    """
    Crée une relation entre item1 et item2 pour Mermaid.
    """
    return f'{item1} --> {item2}'

def ThrowErrorIfMissing(arg:str,errorMessage:str):
    try :
        if arg == None :
            raise Exception(errorMessage)
    except Exception as e:
        print("Error: "+ e.args[0])
        exit()

def generateMermaid(graph, parent=None):
    mermaid_str = ''
    for node, details in graph.items():
        nodeInfo = details["info"]
        node_type = nodeInfo["type"]
        node_name = nodeInfo.get("name", node)
        node_description = nodeInfo["description"]
        mermaid_str += createMermaidDefFor(node, f'{node_type}: {node_name}\ndescription: {node_description}') + '\n'
        
        # Si ce nœud a un parent, on créer la relation enfant parent 
        if parent:
            mermaid_str += createMermaidRelationFor(parent, node) + '\n'
        
        # Récursion pour les enfants, fonction recursive qui vient effectuer le meme travail que sur le parent
        if details["content"]: 
            mermaid_str += generateMermaid(details["content"], node)
    return mermaid_str

def exploreGraph(graph, path, projectJson):
    projectName = projectJson["name"]
    current_level = graph
    current_level_Path = ""
    for node in path:
        current_level_Path += node +"_"
        if current_level_Path not in current_level:
            if node == path[-1]:  # Dernier élément, donc le projet ou groupe spécifique
                current_level[current_level_Path] = {"info": {"type": "project", "name": projectName,"description":projectJson["description"],"fullPath":current_level_Path}, "content": {}}
            else:  # Un groupe intermédiaire
                current_level[current_level_Path] = {"info": {"type": "group","name":current_level_Path,"description":"group node"}, "content": {}}
        current_level = current_level[current_level_Path]["content"]
    return graph


# python3 graphCreator.py -in projetsgitlab.json -pathStartsWith "" -outFile graph.md
if __name__ == "__main__":
    argParser = ArgParser()
    argParser.parse()

    ThrowErrorIfMissing(argParser.entryDict.get("-in"),"No gitlab project json file were supplied, supply it with -in <path> as option of this command")
    inputFIle = argParser.entryDict.get("-in")

    pathStartsWith = ""
    ThrowErrorIfMissing(argParser.entryDict.get("-pathStartsWith"),"No -pathStartsWith <path> as option of this command")
    pathStartsWith = argParser.entryDict.get("-pathStartsWith")

    graphFile = "graph.mmd"
    if argParser.entryDict.get("-outFile"):
        graphFile = argParser.entryDict.get("-outFile")

    gitlabJson = json.load(open(inputFIle))
    flatGraph = []
    for i,index in enumerate(gitlabJson):
        if str(gitlabJson[i]["path_with_namespace"]).startswith(pathStartsWith):
            flatGraph.append((index,gitlabJson[i]["path_with_namespace"]))
    

    finalGraph = {}
    for i,index in enumerate(gitlabJson):
        if str(gitlabJson[i]["path_with_namespace"]).startswith(pathStartsWith):
            project =  gitlabJson[i]
            decomposedPath =project["path_with_namespace"].split("/")
            name = project["name"]
            finalGraph = exploreGraph(finalGraph, decomposedPath,project)

    #log the json graph

    outputJsonGraph = open("outGraph.json",'w')
    outputJsonGraph.write(str(finalGraph).replace("'",'"'))

    mermaid_graph = generateMermaid(finalGraph)

    with open(graphFile, 'w') as mermaidfile:
        mermaidfile.write("```mermaid\n")
        mermaidfile.write("classDiagram\n")
        mermaidfile.write(mermaid_graph)
        mermaidfile.write("```\n")

    print(f"Done. outputed in {graphFile}")