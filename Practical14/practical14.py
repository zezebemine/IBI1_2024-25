
# import necessary libraries
from datetime import datetime
import xml.sax
import xml.dom.minidom

xml_file="D:\\IBI1\\IBI1_2024-25\\Practical14\\go_obo.xml"

# ===== DOM API analysis =====
dom_start_time=datetime.now()

# parse the XML file
dom_tree=xml.dom.minidom.parse(xml_file)

# initialise counters for each namespace
dom_namespace_data={
    'molecular_function':{'max_count':0, 'term_id':'', 'term_name': ''},
    'biological_process':{'max_count':0, 'term_id':'', 'term_name': ''},
    'cellular_component':{'max_count':0, 'term_id':'', 'term_name': ''}
}

# fetch all elements of term
terms=dom_tree.getElementsByTagName('term')

for term in terms:
    # fetch namespace
    namespace=term.getElementsByTagName('namespace')[0].firstChild.nodeValue
    
    # calculate the count of is_a
    is_a_elements=term.getElementsByTagName('is_a')
    count=len(is_a_elements)

    # update max if current count is higher
    if count>dom_namespace_data[namespace]['max_count']:
        dom_namespace_data[namespace]['max_count']=count
        term_id=term.getElementsByTagName('id')[0].firstChild.nodeValue
        term_name=term.getElementsByTagName('name')[0].firstChild.nodeValue
        dom_namespace_data[namespace]['term_id']=term_id
        dom_namespace_data[namespace]['term_name']=term_name

dom_end_time=datetime.now()
dom_duration=dom_end_time-dom_start_time

# =====SAX API analysis=====
sax_start_time=datetime.now()

# creat SAX readers class
class GOTermHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data="" # current analysing tag name
        self.namespace=""
        self.term_id=""
        self.term_name=""
        self.is_a_count=0

        self.namespace_data={
            'molecular_function':{'max_count':0, 'term_id':'', 'term_name': ''},
            'biological_process':{'max_count':0, 'term_id':'', 'term_name': ''},
            'cellular_component':{'max_count':0, 'term_id':'', 'term_name': ''}
        }

    # start element event processing
    def startElement(self, tag, attributes):
        self.current_data=tag # record current analysing tag name 
        if tag=="name":
            self.term_name=""
        elif tag=="id":
            self.term_id=""
        elif tag=="namespace":
            self.namespace=""
        elif tag=="is_a":
            self.is_a_count+=1

    # character data processing
    def characters(self, content):
        # accumulate content according to the current tag
        if self.current_data=="id":
            self.term_id+=content
        elif self.current_data=="name":
            self.term_name+=content
        elif self.current_data=="namespace":
            self.namespace+=content

    # end element event processing
    def endElement(self, tag):
        if tag=="term": # when encourting </term>, mean a whole term element over
            if self.namespace in self.namespace_data:
                # update max if current count is higher
                if self.is_a_count>self.namespace_data[self.namespace]['max_count']:
                    self.namespace_data[self.namespace]['max_count']=self.is_a_count
                    self.namespace_data[self.namespace]['term_id']=self.term_id
                    self.namespace_data[self.namespace]['term_name']=self.term_name

            # initialse to process next term
            self.term_id=""
            self.term_name=""
            self.namespace=""
            self.is_a_count=0
        # clear current_data
        self.current_data=""

# creat readers
reader=xml.sax.make_parser()
reader.setFeature(xml.sax.handler.feature_namespaces,0)

# set process
handler=GOTermHandler()
reader.setContentHandler(handler)

# read file
reader.parse(xml_file)

sax_end_time=datetime.now()
sax_duration=sax_end_time-sax_start_time
        
# ===== print results =====
print("\nResults using DOM API (time:{:.4f} seconds):".format(dom_duration.total_seconds()))
print("-"*60)
for namespace, info in dom_namespace_data.items():
    print(f"Nmaspace: {namespace.title()}")
    print(f"Term ID: {info['term_id']}")
    print(f"Term Name: {info['term_name']}")
    print(f"Number of is_a: {info['max_count']}")

print("\nResults using RAX API (time: {:.4f}) seconds):".format(sax_duration.total_seconds()))
print("-"*60)
for namespace, info in handler.namespace_data.items():
    print(f"Nmaspace: {namespace.title()}")
    print(f"Term ID: {info['term_id']}")
    print(f"Term Name: {info['term_name']}")
    print(f"Number of is_a: {info['max_count']}")

# compare used time
# SAX API was faster than DOM API.
if dom_duration<sax_duration:
    print("\nDOM API was faster than SAX API")
else:
    print("\nSAX API was faster than DOM API")
