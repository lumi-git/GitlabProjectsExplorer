# GitlabProjectsExplorer
Allow to explore projet and output a mermaid graph

## Example launch command

```bash
python3 graphCreator.py -in exampleProjects.json -pathStartsWith "" -outFile graph.md
```

this will output the mermaid graph in the file graph.md, and based on the exampleProjects.json file that represents the returned request from the gitlab project api.


Specify the pathStartWtih to prune the tree from a specific root
