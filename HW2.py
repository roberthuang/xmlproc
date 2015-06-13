from __future__ import division
import xml.etree.ElementTree as ET
import sys,os,ast
from coverage import coverage
passinput=[("xpcmd.py", "XMLData/passing/com.adobe.versioncue.plist"),
           ("xpcmd.py", "XMLData/passing/com.apple.AppleFileServer.plist"),
           ("xpcmd.py", "XMLData/passing/com.apple.BezelServices.plist"),
           ("xpcmd.py", "XMLData/passing/com.apple.ByteRangeLocking.plist"),
           ("xpcmd.py", "XMLData/passing/com.apple.dockfixup.plist"),
           ("xpcmd.py", "XMLData/passing/com.apple.HIToolbox.plist"),
           ("xpcmd.py", "XMLData/passing/com.apple.iWork.Installer.plist"),
           ("xpcmd.py", "XMLData/passing/com.apple.keyboardtype.plist"),
           ("xpcmd.py", "XMLData/passing/com.apple.Keynote.plist"),
           ("xpcmd.py", "XMLData/passing/com.apple.networkConfig.plist"),
           ("xpcmd.py", "XMLData/passing/com.apple.print.defaultpapersize.plist"),
           ("xpcmd.py", "XMLData/passing/com.apple.print.FaxPrefs.plist"),
           ("xpcmd.py", "XMLData/passing/com.apple.RemoteManagement.plist"),
           ("xpcmd.py", "XMLData/passing/com.apple.SetupAssistant.plist"),
           ("xpcmd.py", "XMLData/passing/com.apple.SoftwareUpdate.plist"),
           ("xpcmd.py", "XMLData/passing/com.apple.windowserver.plist"),
           ("xpcmd.py", "XMLData/passing/com.apple.xgrid.agent.plist"),
           ("xpcmd.py", "XMLData/passing/com.apple.xgrid.controller.plist"),
           ("xpcmd.py", "XMLData/passing/com.skype.skype.plist")]




failinput=[("xpcmd.py", "XMLData/failing/com.apple.Asteroid.plist"),
           ("xpcmd.py", "XMLData/failing/com.apple.Cell.plist"),
           ("xpcmd.py", "XMLData/failing/com.apple.Tiger.plist")]

def calling(args):
	#start for coverage 
	cov=coverage()
	cov.start()
	
	sys.argv=args
	
	execfile(sys.argv[0])
	
	#end for coverage and output 'coverage.xml'	
	cov.stop()
	cov.report()
	cov.xml_report()




if __name__ == "__main__":
	passData={}
	failData={}
	
	#for passing
	for item in passinput:
		
		calling(item)
		tree=ET.parse('coverage.xml')
		root=tree.getroot()
		packages=root[1]
		for package in packages:
			for classes in package:
				for class_ in classes:
					test={}
					lines=class_[1]
					if class_.attrib['filename'] in passData.keys():
						#load test from passData
						test=ast.literal_eval(str(passData[class_.attrib['filename']]))
						for line in lines:
							if line.attrib['hits']=='1':
								if line.attrib['number'] in test.keys():
									test[line.attrib['number']]=test[line.attrib['number']]+1
								else:
									test[line.attrib['number']]=1
						passData[class_.attrib['filename']]=test
					
					
					else:
						for line in lines:
							if line.attrib['hits']=='1':
								test[line.attrib['number']]=1
						passData[class_.attrib['filename']]=test		
							
								
	#for faling
	for item in failinput:
		
		calling(item)
		tree=ET.parse('coverage.xml')
		root=tree.getroot()
		packages=root[1]
		for package in packages:
			for classes in package:
				for class_ in classes:
					test={}
					lines=class_[1]
					if class_.attrib['filename'] in failData.keys():
						#load test from failData
						test=ast.literal_eval(str(failData[class_.attrib['filename']]))
						for line in lines:
							if line.attrib['hits']=='1':
								if line.attrib['number'] in test.keys():
									test[line.attrib['number']]=test[line.attrib['number']]+1
								else:
									test[line.attrib['number']]=1
						failData[class_.attrib['filename']]=test
					
					
					else:
						for line in lines:
							if line.attrib['hits']=='1':
								test[line.attrib['number']]=1
						failData[class_.attrib['filename']]=test	
	
	Ns=3
	Nf=19	
	print "\n(a) metric 1:Tarantula\n"	
	rank={}
	for key in failData.keys():
		if key !="HW2.py":
			p = ast.literal_eval(str(passData[key]))
            		f = ast.literal_eval(str(failData[key]))
            		for line in f:
            			#fail test 's number in statement
            			Ncf=f[line]
            			Ncs=p.get(line,0)
            			susp=((float(Ncf) / Nf) / ((float(Ncf) / Nf) + (float(Ncs) / Ns)))
            			s='%s:susp(%s)=%.4f' % (key,line,susp)
				
				print s		
						
						
		
		
		
		
		
		
		
		
		
