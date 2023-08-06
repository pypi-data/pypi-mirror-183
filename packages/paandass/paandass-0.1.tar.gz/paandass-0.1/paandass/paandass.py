class paandass:
    def pgm1(self):
        print('''def aStarAlgo(start_node, stop_node):
        open_set = set(start_node) 
        closed_set = set()
        g = {} 
        parents = {}
        g[start_node] = 0
        parents[start_node] = start_node 
        while len(open_set) > 0 :
            n = None
            for v in open_set:
                if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                    n = v 
            if n == stop_node or Graph_nodes[n] == None:
                pass
            else:
                for (m, weight) in get_neighbors(n):
                    if m not in open_set and m not in closed_set:
                        open_set.add(m)      
                        parents[m] = n       
                        g[m] = g[n] + weight 
                    else:
                        if g[m] > g[n] + weight:
                            g[m] = g[n] + weight
                            parents[m] = n
                            if m in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)
            if n == None:
                print('Path does not exist!')
                return None
            if n == stop_node:
                path = []
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
                path.append(start_node)
                path.reverse()
                print('Path found: {}'.format(path))
                return path
            open_set.remove(n)
            closed_set.add(n)
        print('Path does not exist!')
        return None

    def get_neighbors(v):
        if v in Graph_nodes:
            return Graph_nodes[v]
        else:
            return None

    def heuristic(n):
        H_dist = {
            'S': 5,
            'A': 4,
            'B': 5,
            'E': 0,
        }
        return H_dist[n]
    Graph_nodes = {
        'S': [('A', 1), ('B', 2)],
        'A': [('E', 13),],
        'B': [('E', 5)] 
    }
    aStarAlgo('S', 'E')''')


    def pgm2(self):
        print( '''
        class Graph:
        def __init__(self, graph, heuristicNodeList, startNode):
            self.graph = graph
            self.H=heuristicNodeList
            self.start=startNode
            self.parent={}
            self.status={}
            self.solutionGraph={}
        def applyAOStar(self):
            self.aoStar(self.start, False)
        def getNeighbors(self, v): 
            return self.graph.get(v,'')
        def getStatus(self,v): 
            return self.status.get(v,0)
        def setStatus(self,v, val):
            self.status[v]=val
        def getHeuristicNodeValue(self, n):
            return self.H.get(n,0) 
        def setHeuristicNodeValue(self, n, value):
            self.H[n]=value 

        def printSolution(self):
            print("FOR GRAPH SOLUTION, TRAVERSE THE GRAPH FROM THE STARTNODE:",self.start)
            print("------------------------------------------------------------")
            print(self.solutionGraph)
            print("------------------------------------------------------------")

        def computeMinimumCostChildNodes(self, v):
            minimumCost=0
            costToChildNodeListDict={}
            costToChildNodeListDict[minimumCost]=[]
            flag=True
            for nodeInfoTupleList in self.getNeighbors(v):
                cost=0
                nodeList=[]
                for c, weight in nodeInfoTupleList:
                    cost=cost+self.getHeuristicNodeValue(c)+weight
                    nodeList.append(c)

                if flag==True:
                    minimumCost=cost
                    costToChildNodeListDict[minimumCost]=nodeList 
                    flag=False
                else: 
                    if minimumCost>cost:
                        minimumCost=cost
                        costToChildNodeListDict[minimumCost]=nodeList
            return minimumCost, costToChildNodeListDict[minimumCost] 
    
        def aoStar(self, v, backTracking): 
            print("HEURISTIC VALUES :", self.H)
            print("SOLUTION GRAPH :", self.solutionGraph)
            print("PROCESSING NODE :", v)
            print("-----------------------------------------------------------------------------------------")
            if self.getStatus(v) >= 0: 
                minimumCost, childNodeList = self.computeMinimumCostChildNodes(v)
                self.setHeuristicNodeValue(v, minimumCost)
                self.setStatus(v,len(childNodeList))
                solved=True 
                for childNode in childNodeList:
                    self.parent[childNode]=v
                    if self.getStatus(childNode)!=-1:
                        solved=solved & False
                if solved==True:
                    self.setStatus(v,-1)
                    self.solutionGraph[v]=childNodeList 
                if v!=self.start:
                    self.aoStar(self.parent[v], True) 
                if backTracking==False: 
                    for childNode in childNodeList: 
                        self.setStatus(childNode,0) 
                        self.aoStar(childNode, False) 
    h1 = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I':7,'J':1}
    graph1 = {
        'A': [[('B', 1), ('C', 1)], [('D', 1)]],
        'B': [[('G', 1)], [('H', 1)]],
        'C': [[('J', 1)]],
        'D': [[('E', 1), ('F', 1)]],
        'G': [[('I', 1)]]
    }
    G1= Graph(graph1, h1, 'A')
    G1.applyAOStar()
    G1.printSolution()
    ''')
    def pgm3(self):
        print( '''
    import numpy as np 
    import pandas as pd
    data = pd.read_csv("ws.csv",header=None)
    concepts = np.array(data.iloc[:,0:-1])
    print("\\nInstances are:\\n",concepts)
    target = np.array(data.iloc[:,-1])
    print("\\nTarget Values are: ",target)

    def learn(concepts,target): 
        specific_h = concepts[0].copy()
        print("\\nInitialization of specific_h and genearal_h")
        print("\\nSpecific Boundary: ", specific_h)
        general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
        print("\\nGeneric Boundary: ",general_h)  

        for i,h  in enumerate(concepts):
            print("\\nInstance", i+1 , "is ", h)
            if target[i] == "Yes":
                print("Instance is Positive ")
                for x in range(len(specific_h)): 
                    if h[x]!= specific_h[x]:                    
                        specific_h[x] ='?'                     
                        general_h[x][x] ='?'
                    
            if target[i] == "No":            
                print("Instance is Negative ")
                for x in range(len(specific_h)): 
                    if h[x]!= specific_h[x]:                    
                        general_h[x][x] = specific_h[x]                
                    else:                    
                        general_h[x][x] = '?'        
            
            print("Specific Boundary after ", i+1, "Instance is ", specific_h)         
            print("Generic Boundary after ", i+1, "Instance is ", general_h)
            print("\\n")
        indices = [ i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]   
        for i in indices:   
            general_h.remove(['?', '?', '?', '?', '?', '?']) 
        return specific_h, general_h 
    s_final, g_final = learn(concepts,target)
    print("Final Specific_h: ", s_final, sep="\\n")
    print("Final General_h: ", g_final, sep="\\n")
    ''')

    def pgm4(self):
        print('''
    import math
    import csv
    def load_csv(filename):
        lines = csv.reader(open(filename, "r"));
        dataset = list(lines)
        headers = dataset.pop(0)
        return dataset, headers
    class Node:
        def __init__(self, attribute):
            self.attribute = attribute
            self.children = []
            self.answer = "" 
    def subtables(data, col, delete): 
        dic = {}
        coldata = [ row[col] for row in data]
        attr = list(set(coldata)) 
        for k in attr:
            dic[k] = []
        for y in range(len(data)):
            key = data[y][col]
            if delete:
                del data[y][col]
            dic[key].append(data[y])
        return attr, dic
    def entropy(S):
        attr = list(set(S))
        if len(attr) == 1: 
            return 0
        counts = [0,0] 
        for i in range(2):
            counts[i] = sum( [1 for x in S if attr[i] == x] ) / (len(S) * 1.0)
        sums = 0
        for cnt in counts:
            sums += -1 * cnt * math.log(cnt, 2)
        return sums
    def compute_gain(data, col):
        attValues, dic = subtables(data, col, delete=False)
        total_entropy = entropy([row[-1] for row in data])
        for x in range(len(attValues)):
            ratio = len(dic[attValues[x]]) / ( len(data) * 1.0)
            entro = entropy([row[-1] for row in dic[attValues[x]]]) 
            total_entropy -= ratio*entro
        return total_entropy
    def build_tree(data, features):
        lastcol = [row[-1] for row in data]
        if (len(set(lastcol))) == 1: 
            node=Node("")
            node.answer = lastcol[0]
            return node
        n = len(data[0])-1
        gains = [compute_gain(data, col) for col in range(n) ]
        split = gains.index(max(gains))
        node = Node(features[split]) 
        fea = features[:split]+features[split+1:]
        attr, dic = subtables(data, split, delete=True) 
        for x in range(len(attr)):
            child = build_tree(dic[attr[x]], fea) 
            node.children.append((attr[x], child))
        return node
    def print_tree(node, level):
        if node.answer != "":
            print("     "*level, node.answer) 
            return
        print("       "*level, node.attribute) 
        for value, n in node.children:
            print("     "*(level+1), value) 
            print_tree(n, level + 2)
    def classify(node,x_test,features): 
        if node.answer != "":
            print(node.answer) 
            return

        pos = features.index(node.attribute)
        for value, n in node.children:
            if x_test[pos]==value: 
                classify(n,x_test,features)

    dataset, features = load_csv("data3.csv") 
    node = build_tree(dataset, features) 
    print("The decision tree for the dataset using ID3 algorithm is ") 
    print_tree(node, 0)
    testdata, features = load_csv("data3test.csv") 
    for xtest in testdata:
        print("The test instance : ",xtest) 
        print("The predicted label : ", end="") 
        classify(node,xtest,features)
        ''')

    def pgm5(self):
        print('''
    import numpy as np
    X=np.array(([2,9],[1,5],[3,6]),dtype=float)  
    y=np.array(([92],[86],[89]),dtype=float) 
    X=X/np.amax(X,axis=0)  
    y=y/100
    def sigmoid(x):
        return 1/(1+np.exp(-x))
    def sigmoid_grad(x):
        return x*(1-x)
    epoch=1000  
    eta=0.2    
    input_neurons=2  
    hidden_neurons=3  
    output_neurons=1 
    wh=np.random.uniform(size=(input_neurons,hidden_neurons))
    bh=np.random.uniform(size=(1,hidden_neurons))
    wout=np.random.uniform(size=(hidden_neurons,output_neurons))
    bout=np.random.uniform(size=(1,output_neurons))
    for i in range(epoch):
        h_ip=np.dot(X,wh)+bh
        h_act=sigmoid(h_ip)
        o_ip=np.dot(h_act,wout)+bout
        output=sigmoid(o_ip)
        Eo=y-output
        outgrad=sigmoid_grad(output)
        d_output=Eo*outgrad
        Eh=d_output.dot(wout.T)
        hiddengrad=sigmoid_grad(h_act)
        d_hidden=Eh*hiddengrad
        wout+=h_act.T.dot(d_output)*eta
        wh+=X.T.dot(d_hidden)*eta
    print("Normalized Input:\\n"+str(X))
    print("Actual Output:\\n"+str(y))
    print("Predicted output:\\n",output)
        ''')

    def pgm6(self):
        print('''
    import csv, random, math
    import statistics as st
    from statistics import stdev

    def loadCsv(filename):
        lines = csv.reader(open(filename, "r"));
        dataset = list(lines)
        for i in range(len(dataset)):
            dataset[i] = [float(x) for x in dataset[i]]
        return dataset

    def splitDataset(dataset, splitRatio):
        testSize = int(len(dataset) * splitRatio);
        trainSet = list(dataset)
        testSet = []
        while len(testSet) < testSize:

            index = random.randrange(len(trainSet));
            testSet.append(trainSet.pop(index))
        return [trainSet, testSet]

    def separateByClass(dataset):
        separated = {}
        for i in range(len(dataset)):
            x = dataset[i]
            if (x[-1] not in separated):
                separated[x[-1]] = []
            separated[x[-1]].append(x)
        return separated

    def mean(numbers):
        return sum(numbers)/float(len(numbers))

    def stdev(numbers):
        avg=mean(numbers)
        variance=sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
        return math.sqrt(variance)

    def compute_mean_std(dataset):
        mean_std = [(st.mean(attribute), st.stdev(attribute))for attribute in zip(*dataset)];
        del mean_std[-1] # Exclude label
        return mean_std


    def summarizeByClass(dataset):
        separated = separateByClass(dataset)
        summary = {}
        for classValue, instances in separated.items():
        
            summary[classValue] = compute_mean_std(instances)
        return summary

    def estimateProbability(x, mean, stdev):
        exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
        return (1 / (math.sqrt(2*math.pi) *stdev))*exponent

    def calculateClassProbabilities(summaries, testVector):
        p = {}

        for classValue, classSummaries in summaries.items():
            p[classValue] = 1
            for i in range(len(classSummaries)):
                mean, stdev = classSummaries[i]
                x = testVector[i]
                p[classValue] *= estimateProbability(x, mean, stdev)
        return p
    def predict(summaries, testVector):
        all_p = calculateClassProbabilities(summaries, testVector)
        bestLabel, bestProb = None, -1
        for lbl, p in all_p.items():
            if bestLabel is None or p > bestProb:
                bestProb = p
            bestLabel = lbl
        return bestLabel

    def perform_classification(summaries, testSet):
        predictions = []
        for i in range(len(testSet)):
            result = predict(summaries, testSet[i])
            predictions.append(result)
        return predictions

    def getAccuracy(testSet, predictions):
        correct = 0
        for i in range(len(testSet)):
            if testSet[i][-1] == predictions[i]:
                correct += 1
        return(correct/float(len(testSet))) * 100.0

    dataset = loadCsv('pima-indians-diabetes.csv')
    print('Pima Indian Diabetes Dataset loaded...')
    print('Total instances available :',len(dataset))
    print('Total attributes present :',len(dataset[0])-1)
    print("First Five instances of dataset:")
    for i in range(5):
        print(i+1 , ':' , dataset[i])

    splitRatio = 0.2
    trainingSet, testSet = splitDataset(dataset, splitRatio)
    print('\\nDataset is split into training and testing set.')
    print('Training examples = {0} \\nTesting examples = {1}'.format(len(trainingSet), len(testSet)))
    summaries = summarizeByClass(trainingSet)
    predictions = perform_classification(summaries, testSet)
    accuracy = getAccuracy(testSet, predictions)
    print('\\nAccuracy of the Naive Baysian Classifier is :', accuracy)
        ''')

    def pgm7(self):
        print('''
    import matplotlib.pyplot as plt
    from sklearn import datasets
    from sklearn.cluster import KMeans
    import pandas as pd
    import numpy as np
    iris=datasets.load_iris()
    X=pd.DataFrame(iris.data)
    X.columns=['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']
    y=pd.DataFrame(iris.target)
    y.columns=['Targets']
    model=KMeans(n_clusters=3)
    model.fit(X)
    plt.figure(figsize=(14,14))
    colormap=np.array(['red','lime','black'])
    plt.subplot(2,2,1)
    plt.scatter(X.Petal_Length, X.Petal_Width,c=colormap[y.Targets],s=40)
    plt.title('Real Clusters')
    plt.xlabel('Petal Length')
    plt.ylabel('Petal Width')
    plt.subplot(2,2,2)
    plt.scatter(X.Petal_Length,X.Petal_Width,c=colormap[model.labels_],s=40)
    plt.title('K-means Clustering')
    plt.xlabel('Petal Length')
    plt.ylabel('Petal Width')
    from sklearn import preprocessing
    scaler=preprocessing.StandardScaler()
    scaler.fit(X)
    xsa=scaler.transform(X)
    xs=pd.DataFrame(xsa,columns=X.columns)
    from sklearn.mixture import GaussianMixture
    gmm=GaussianMixture(n_components=3)
    gmm.fit(xs)
    gmm_y=gmm.predict(xs)
    plt.subplot(2,2,3)
    plt.scatter(X.Petal_Length,X.Petal_Width,c=colormap[gmm_y],s=40)
    plt.title('GMM Clustering')
    plt.xlabel('Petal Length')
    plt.ylabel('Petal Width')
    print("Observation:The GMM using EM algorithm based clustering matched the true labels more closely than Kmeans")
    plt.show()
        ''')


    def pgm8(self):
        print('''
    from sklearn.datasets import load_iris
    from sklearn.neighbors import KNeighborsClassifier
    import numpy as np
    from sklearn.model_selection import train_test_split
    iris_dataset=load_iris()

    print("\\n IRIS FEATURES \ TARGET NAMES: \\n ", iris_dataset.target_names)
    for i in range(len(iris_dataset.target_names)):
        print("\\n[{0}]:[{1}]".format(i,iris_dataset.target_names[i]))

    print("\\n IRIS DATA :\\n",iris_dataset["data"])
    X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state=0)
    print("\\n Target :\\n",iris_dataset["target"])
    print("\\n X TRAIN \\n", X_train)
    print("\\n X TEST \\n", X_test)
    print("\\n Y TRAIN \\n", y_train)
    print("\\n Y TEST \\n", y_test)
    kn = KNeighborsClassifier(n_neighbors=1)
    kn.fit(X_train,y_train )

    x_new = np.array([[5, 2.9, 1, 0.2]])
    print("\\n XNEW \\n",x_new)
    prediction = kn.predict(x_new)
    print("\\n Predicted target value: {}\\n".format(prediction))
    print("\\n Predicted feature name: {}\\n".format(iris_dataset["target_names"][prediction]))
    i=1
    x= X_test[i]
    x_new = np.array([x])
    print("\\n XNEW \\n",x_new)

    for i in range(len(X_test)):
        x = X_test[i]
        x_new = np.array([x])
        prediction = kn.predict(x_new)
        print("\\n Actual : {0} {1}, Predicted :{2}{3}".format(y_test[i],iris_dataset["target_names"][y_test[i]],prediction,iris_dataset["target_names"][prediction]))
    print("\\n TEST SCORE[ACCURACY]: {:.2f}\\n".format(kn.score(X_test, y_test)))
        ''')


    def pgm9(self):
        print('''
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    def kernel(point,xmat,k):
        m,n = np.shape(xmat)
        weights = np.mat(np.eye((m)))
        for j in range(m):
            diff=point - X[j]
            weights[j,j] = np.exp(diff*diff.T/(-2.0*k**2))
        return weights

    def localWeight(point,xmat,ymat,k):
        wei=kernel(point,xmat,k)
        W=(X.T*(wei*X)).I*(X.T*(wei*ymat.T))
        return W

    def localweightregression(xmat,ymat,k):
        m,n=np.shape(xmat)
        ypred=np.zeros(m)
        for i in range(m):
            ypred[i]=xmat[i]*localWeight(xmat[i],xmat,ymat,k)
        return ypred

    def graphplot(X,ypred):
        sortindex=X[:,1].argsort(0)
        xsort=X[sortindex][:,0]
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)
        ax.scatter(bill,tip,color='green')
        ax.plot(xsort[:,1],ypred[sortindex],color='red',linewidth=4)
        plt.xlabel('Total Bill')
        plt.ylabel('Tip')
        plt.show()

    data=pd.read_csv('data10_tips.csv')
    bill=np.array(data.total_bill)
    tip=np.array(data.tip)
    mbill=np.mat(bill)
    mtip=np.mat(tip)
    m=np.shape(mbill)[1]
    one=np.mat(np.ones(m))
    X=np.hstack((one.T,mbill.T))
    ypred=localweightregression(X,mtip,0.5)
    graphplot(X,ypred)
        ''')

