import tcxparser
from lxml import objectify
from lxml import etree

base_file = './Sample Data/runtastic_20160303_0007_Running.tcx'

s = open(base_file)
g = s.read()

tcx = tcxparser.TCXParser(base_file)

tree = objectify.parse(base_file)

print g
tree1 = etree.XML(g)
time = tree1.xpath('TrainingCenterDatabase/Activities/Activity/Lap/Track/Trackpoint/Time/text()')

print(time)



print type(tree.getroot().Activities.Activity.Lap.Track.Trackpoint.Position)


#print tcx.latitude
