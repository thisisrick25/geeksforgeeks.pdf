import json
from links import grab_links


gate_topics = [
    "http://www.geeksforgeeks.org/tag/operating-systems/",
    "http://www.geeksforgeeks.org/tag/DBMS/",
    "http://www.geeksforgeeks.org/tag/AT/",
    "http://www.geeksforgeeks.org/tag/compilers/",
    "http://www.geeksforgeeks.org/tag/CN/",
    "http://www.geeksforgeeks.org/tag/gate-cs-ds-algo/",
    "http://www.geeksforgeeks.org/tag/gate-cs-ds-algo/page/2/"
]

interview = [
    "http://www.geeksforgeeks.org/tag/payu/",
    "http://www.geeksforgeeks.org/tag/adobe/",
    "http://www.geeksforgeeks.org/tag/amazon/",
    "http://www.geeksforgeeks.org/tag/flipkart/",
    "http://www.geeksforgeeks.org/tag/google/",
    "http://www.geeksforgeeks.org/tag/microsoft/",
    "http://www.geeksforgeeks.org/tag/snapdeal/",
    "http://www.geeksforgeeks.org/tag/zopper-com/",
    "http://www.geeksforgeeks.org/tag/yahoo/",
    "http://www.geeksforgeeks.org/tag/cisco/",
    "http://www.geeksforgeeks.org/tag/facebook/",
    "http://www.geeksforgeeks.org/tag/yatra.com/",
    "http://www.geeksforgeeks.org/tag/Symantec/",
    "http://www.geeksforgeeks.org/tag/myntra/",
    "http://www.geeksforgeeks.org/tag/Groupon/",
    "http://www.geeksforgeeks.org/tag/Belzabar/",
    "http://www.geeksforgeeks.org/tag/paypal/",
    "http://www.geeksforgeeks.org/tag/akosha/",
    "http://www.geeksforgeeks.org/tag/linkedin/",
    "http://www.geeksforgeeks.org/tag/BrowserStack/",
    "http://www.geeksforgeeks.org/tag/MakeMyTrip/",
    "http://www.geeksforgeeks.org/tag/InfoEdge/",
    "http://www.geeksforgeeks.org/tag/practo/",
    "http://www.geeksforgeeks.org/tag/housing-com/",
    "http://www.geeksforgeeks.org/tag/ola-cabs/",
    "http://www.geeksforgeeks.org/tag/grofers/",
    "http://www.geeksforgeeks.org/tag/thoughtworks/",
    "http://www.geeksforgeeks.org/tag/delhivery/",
    "http://www.geeksforgeeks.org/tag/taxi4sure/",
    "http://www.geeksforgeeks.org/tag/lenskart/",
]

dp = [
    "http://www.geeksforgeeks.org/tag/dynamic-programming/",
    "http://www.geeksforgeeks.org/tag/dynamic-programming/page/2/",
    "http://www.geeksforgeeks.org/tag/dynamic-programming/page/3/",
    "http://www.geeksforgeeks.org/tag/dynamic-programming/page/4/",
    "http://www.geeksforgeeks.org/tag/dynamic-programming/page/5/",
]


if __name__ == '__main__':
    grab_links(dp, "DynamicProgramming.json")
