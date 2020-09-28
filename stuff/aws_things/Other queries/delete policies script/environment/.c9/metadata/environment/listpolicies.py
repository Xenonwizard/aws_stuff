{"filter":false,"title":"listpolicies.py","tooltip":"/listpolicies.py","undoManager":{"mark":31,"position":31,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["i"],"id":1},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["m"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["p"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["o"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["r"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":[" "],"id":2},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["b"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["o"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["t"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["o"]},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["3"]}],[{"start":{"row":0,"column":12},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":1,"column":0},"end":{"row":5,"column":40},"action":"insert","lines":["import json,boto3"," ","client = boto3.client('iam')","# while True:","data=client.list_policies(Scope='Local')"],"id":4}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":12},"action":"remove","lines":["import boto3"],"id":5},{"start":{"row":5,"column":40},"end":{"row":6,"column":0},"action":"insert","lines":["",""]},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":7,"column":0},"end":{"row":9,"column":39},"action":"insert","lines":["for x in data['Policies']:","    ","         client.delete_policy(x['Arn'])"],"id":6}],[{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"remove","lines":["e"],"id":7},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"remove","lines":["t"]},{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"remove","lines":["e"]},{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"remove","lines":["l"]},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"remove","lines":["e"]},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"remove","lines":["d"]}],[{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":["l"],"id":8},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["i"]},{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"insert","lines":["s"]},{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":9,"column":16},"end":{"row":9,"column":20},"action":"remove","lines":["list"],"id":9},{"start":{"row":9,"column":16},"end":{"row":9,"column":29},"action":"insert","lines":["list_policies"]}],[{"start":{"row":9,"column":29},"end":{"row":9,"column":46},"action":"remove","lines":["_policy(x['Arn'])"],"id":10}],[{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":["9"],"id":11},{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"insert","lines":["0"]}],[{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"remove","lines":["0"],"id":12},{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"remove","lines":["9"]}],[{"start":{"row":9,"column":29},"end":{"row":9,"column":31},"action":"insert","lines":["()"],"id":13}],[{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"remove","lines":[")"],"id":14},{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"remove","lines":["("]},{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"remove","lines":["s"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"remove","lines":["e"]},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"remove","lines":["i"]},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"remove","lines":["c"]},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"remove","lines":["i"]},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"remove","lines":["l"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"remove","lines":["o"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"remove","lines":["p"]},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"remove","lines":["_"]},{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"remove","lines":["t"]},{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"remove","lines":["s"]},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"remove","lines":["i"]},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"remove","lines":["l"]},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"remove","lines":["."]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"remove","lines":["t"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"remove","lines":["n"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"remove","lines":["e"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"remove","lines":["i"]},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"remove","lines":["l"]},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"remove","lines":["c"]},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"remove","lines":[" "]}],[{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["p"],"id":15},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["r"]},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["u"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["b"]}],[{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"remove","lines":["b"],"id":16},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"remove","lines":["u"]},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"remove","lines":["r"]},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"remove","lines":["p"]},{"start":{"row":9,"column":4},"end":{"row":9,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["p"],"id":17},{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["r"]},{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["i"]},{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":["n"]},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":11},"action":"insert","lines":["()"],"id":18}],[{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["x"],"id":19}],[{"start":{"row":9,"column":11},"end":{"row":9,"column":13},"action":"insert","lines":["[]"],"id":20}],[{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["P"],"id":21},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["o"]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"insert","lines":["l"]},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"insert","lines":["i"]},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":["c"]},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["e"]},{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"insert","lines":["="]}],[{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"remove","lines":["="],"id":22},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"remove","lines":["e"]}],[{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["t"],"id":23}],[{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"remove","lines":["t"],"id":24}],[{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["y"],"id":25},{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"insert","lines":["N"]},{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"insert","lines":["a"]},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"insert","lines":["m"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["e"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["'"]}],[{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["'"],"id":26},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":[";"]}],[{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"remove","lines":[";"],"id":27}],[{"start":{"row":9,"column":26},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":28},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["p"]},{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":["r"]},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["i"]},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["n"]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":10,"column":9},"end":{"row":10,"column":11},"action":"insert","lines":["()"],"id":29}],[{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["n"],"id":30},{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["o"]},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["n"]}],[{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"remove","lines":[")"],"id":31},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"remove","lines":["n"]},{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"remove","lines":["o"]},{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"remove","lines":["n"]},{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"remove","lines":["("]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"remove","lines":["t"]},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"remove","lines":["n"]},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"remove","lines":["i"]},{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"remove","lines":["r"]},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"remove","lines":["p"]}],[{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"remove","lines":["]"],"id":32},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"remove","lines":["'"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"remove","lines":["e"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"remove","lines":["m"]},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"remove","lines":["a"]},{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"remove","lines":["N"]},{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"remove","lines":["y"]},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"remove","lines":["c"]},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"remove","lines":["i"]},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"remove","lines":["l"]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"remove","lines":["o"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"remove","lines":["P"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"remove","lines":["'"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"remove","lines":["["]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":11},"end":{"row":9,"column":11},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":11,"mode":"ace/mode/python"}},"timestamp":1601017756025,"hash":"a7302a00e3bc3b575575b05fbc8a0f95bb7783c7"}