#DOM
'''
record the start time start_time = the current time
parse the xml file to obtain the dom_tree and acquire the document element of the root element collection = dom_tree
obtain all <term> elements. terms = collection obtain all elements with the tag name "term"
the initialization of the maximum term list max_terms contains three namespaces, and each namespace corresponds to an empty term list
traverse each <term> element. term is in terms:
obtain the namespace namespace = term. obtain the text content of the first child element with the tag name "namespace"
obtain the term id term_id = term. obtain the text content of the first child element with the label name "id"
obtain the term name term_name = term. obtain the text content of the first child element with the label name" name"
obtain all <is_a> elements is_a_list = term obtain the list of elements with the tag name "is_a"
calculate the length of the <is_a> element number is_a_count = is_a_list
traverse each item in the maximum term list max_terms
record the end time: end_time = current time
print "-- dom results --"
print "dom processing time: "the time difference between the end time end_time and the start time start_time
'''
#import necessary library
import xml.dom.minidom
from datetime import datetime
#record start time
start_time = datetime.now()
#obtain the dom_tree and root element
dom_tree = xml.dom.minidom.parse("/Users/cuilizi/Desktop/Lecture/IBI/IBI1/IBI1_2024-25/IBI1_2024-25/Practical14/go_obo.xml")
collection = dom_tree.documentElement
terms = collection.getElementsByTagName("term")
#the initialization of the max_terms contains three namespaces
max_terms = [
    {"namespace": "molecular_function","terms": []},
    {"namespace": "biological_process","terms": []},
    {"namespace": "cellular_component","terms": []}
]
#traverse each term element
for term in terms:
    namespace = term.getElementsByTagName("namespace")[0].firstChild.data
    term_id = term.getElementsByTagName("id")[0].firstChild.data
    term_name = term.getElementsByTagName("name")[0].firstChild.data
    is_a_list = term.getElementsByTagName("is_a")
    is_a_count = len(is_a_list)
    #Traverse each item in max_terms
    for item in max_terms:
        if item["namespace"] == namespace:
            current_max = max((t.get("count", 0) for t in item["terms"]), default=0)
            #get the max data
            if is_a_count > current_max:
                item["terms"] = [{"id": term_id, "name": term_name, "count": is_a_count}]
            elif is_a_count == current_max:
                item["terms"].append({"id": term_id, "name": term_name, "count": is_a_count})
            break
#record end time and print the result
end_time = datetime.now()
print("\n--- DOM Results ---")
for item in max_terms:
    namespace = item["namespace"]
    for term_info in item["terms"]:
        print(f"{namespace}:")
        print(f"  ID: {term_info['id']}")
        print(f"  Name: {term_info['name']}")
        print(f"  is_a count: {term_info['count']}")
#calculate the time
print(f"\nDOM Processing Time: {end_time - start_time}")

#SAX
'''
define the gohandler class:
initialize the max_terms dictionary and store the terms with the maximum is_a count by namespace classification
when encountering the <term> tag,reset the namespace, id, name and is_a count of the current term
when parsing the text within the label, according to the current tag type (id/name/namespace/is_a)
accumulate and store the id, name, and namespace text
if it is the "is_a" tag, increase the count
when encountering the <term> tag:
according to the namespace of the current term:
if the is_a count of the term is greater than the maximum value of the current record:
update the maximum record of this namespace to the current term
if the counts are the same:
add the current term to the parallel record of this namespace
create a sax parser and register the processor, open and parse the go xml file
traverse each namespace:
print the term information (id, name, count) with the maximum is_a count
'''
#import library
import xml.sax
from datetime import datetime
#record start time
start_time = datetime.now()
#define the GoHandler class
class GoHandler(xml.sax.ContentHandler):
    #initialize the max_terms dictionary
    def __init__(self):
        self.namespace = ""
        self.term_id = ""
        self.term_name = ""
        self.is_a_count = 0

        self.max_terms = [
            {"namespace": "molecular_function", "terms": []},
            {"namespace": "biological_process", "terms": []},
            {"namespace": "cellular_component", "terms": []}
        ]

        self.current_element = ""
        self.in_term = False
        self.name_buffer = ""
    #when encountering the <term> tag,reset the namespace, ID, name and is_a count of the current term
    def startElement(self, tag, attrs):
        self.current_element = tag
        if tag == "term":
            self.in_term = True
            self.namespace = ""
            self.term_id = ""
            self.term_name = ""
            self.is_a_count = 0
            self.name_buffer = ""
    #when parsing the text within the label,accumulate and store the ID, name, and namespace text
    def characters(self, content):
        if self.in_term:
            if self.current_element == "id":
                self.term_id += content.strip()
            elif self.current_element == "name":
                self.name_buffer += content.strip()
            elif self.current_element == "namespace":
                self.namespace += content.strip()
            elif self.current_element == "is_a":
                self.is_a_count += 1
    #record the results
    def endElement(self, tag):
        if tag == "term":
            for item in self.max_terms:
                if item["namespace"] == self.namespace:
                    new_term = {"id": self.term_id, "name": self.name_buffer, "count": self.is_a_count}
                    if not item["terms"]:
                        item["terms"].append(new_term)
                    else:
                        current_max = max(t["count"] for t in item["terms"])
                        if self.is_a_count > current_max:
                            item["terms"] = [new_term]
                        elif self.is_a_count == current_max:
                            item["terms"].append(new_term)
                    break
            self.in_term = False
        self.current_element = ""
#analyze and process, and record the time
parser = xml.sax.make_parser()
handler = GoHandler()
parser.setContentHandler(handler)
parser.parse("/Users/cuilizi/Desktop/Lecture/IBI/IBI1/IBI1_2024-25/IBI1_2024-25/Practical14/go_obo.xml")
end_time = datetime.now()
#print the result
print("\n--- SAX Results ---")
for item in handler.max_terms:
    namespace = item["namespace"]
    terms_data = item["terms"]
    print(f"{namespace}:")
    for term in terms_data:
        print(f"  ID: {term['id']}")
        print(f"  Name: {term['name']}")
        print(f"  is_a count: {term['count']}")

print(f"\nSAX Processing Time: {end_time - start_time}")

## The SAX is faster than the DOM.