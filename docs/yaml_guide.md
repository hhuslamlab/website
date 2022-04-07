
# A quick guide to YAML 

# Table of Contents
- [Introduction](#Introduction)
- [Working with YAML Files](#working)
- [Data Types in YAML Files](#datatypes)
    - [Strings](#strings)
    - [Lists](#lists)
    - [Dicts](#dicts)
- [Resources](#resources)



## Introduction <a name="Introduction"></a>
YAML (Yaml Ain't Markup Language) is a markup language specially designed for data serialization purposes. File extentions for YAML files can both be `.yml`and `.yaml`. They are generally used for configuration files and Docker, for example.

## Working with YAML files<a name="working"></a>
To work with YAML files, you have to download the <a href="https://pyyaml.org/">PyYaml module</a> and import it with`import pyaml`. 
You can read a YAML file with:
```python
import yaml

with open('items.yaml') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
```
There is no good way of appending a YAML file. Writing in a YAML file always means overwriting the previous content, if there was some.
```python
import yaml

users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]

print(yaml.dump(users))

#prints in yaml file as: 
- name: John Doe
  occupation: gardener
- name: Lucy Black
  occupation: teacher
```
The script from <a href="https://pyyaml.org/">a tutorial</a> shows how to load and manipulate data. 
```python
def yaml_loader(filepath):

	with open(filepath, "r") as file_descriptor:
		data= yaml.load(file_descriptor)
	return data

def yaml_dump(filepath, data):
	with open(filepath, "w") as file_descriptor:
		yaml.dump(data, file_descriptor)
if __name__ == "__main__":
	file_path = "test.yaml"
	print data

#more like the format of data in the yaml file 
	items = data.get("items")
	for item_name, item_value in items.iteritems():
		print item_name, item_value 

	filepath2 = "test2.yaml"
	data2 = {
	    "items": {
			"sword": 100,
			"axe": 80,
			"boots": 40
				}
	        }

yaml_dump(filepath2, data2)
```
Here is another one from <a href="https://www.youtube.com/watch?v=rQ3U5VEGg7Q">a different tutorial</a> on how to process data in chunks:
```python 
import yaml

with open(r "data.yaml") as file: 
	user_list = yaml.load(file, loader =yaml.FullLoader)
	print(user_list)

	print(type(user.list))
		#but we want a list not a dictionary to prrocess it in chunks 

with open(r "data.yaml") as file: 
	user_list = yaml.load(file, loader =yaml.FullLoader)
	print(user_list["user"])
#list of users only 

def chunks(list, n):
	for i in range(0, len(list), n):
		yield list[i:i+n]
for accounts in chunks (user_list["user"], 4) #4 is n
	print(accounts) # prints chunks of four 
```

## Data Types in YAML files<a name="datatypes"></a>
### Strings<a name="strings"></a>
* Are recognized automatically, quotations can optionally be added
```yaml
color: red
```
* Multiline strings can be broken up by the `>` sign and pressing `enter` 
* That way, the string can be broken into however many lines but still be recognized as one string
```yaml
background: >
Founded in 19383 this is 
something fictional 
```
* If you want the line breaks to be preserved, you can use the `|` symbol 

```yaml
background: | 
Founded in 19383 this is 
something fictional 
```

### Lists<a name="lists"></a>
* Lists are denoted by `space` and one dash `-` or the `[]`notation
```Yaml
fruits: 
- apple
- clementine

#OR

fruits: [mango, papaya, avocado]
```
*lists of objects are written in a similar way:
```YAML
fruits: 
 - name: banana
   color: yellow
 - name: plum
   color: purple
```

### Dicts<a name="dicts"></a>
```YAML
management_staff:
 general_manager: Elon Musk
```

## Resources<a name="resources"></a>
<a href="https://yamlchecker.com/">YAML syntax checker</a> 
<a href="https://onlinexmltools.com/">Convert YAML to XML and other languages</a> 
<a href="https://jsonformatter.org/yaml-to-json">Convert YAML to JSON</a> 
