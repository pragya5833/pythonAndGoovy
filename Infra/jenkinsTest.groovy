import groovy.json.JsonSlurper
def get = new URL("https://api.github.com/repos/pragya5833/EF_Assignment/git/trees/master").openConnection();
def getRC = get.getResponseCode();
if (getRC.equals(200)) {
    y=get.getInputStream().getText();
}
def jsonSlurper = new JsonSlurper()
def object = jsonSlurper.parseText (y)
def z=object.tree
def arrayLength = z.size()
def myList=['1']
for (i = 0; i <arrayLength; i++){
myList.add(z[i].path.toString())
}
return myList
