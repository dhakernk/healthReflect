import json

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from urllib2 import Request, urlopen
import numpy as np
def index(request):
	context = {}
	return render_to_response('test.html', context, context_instance=RequestContext(request))

@csrf_protect
def getTopCollageList(request):
	"""Return top Collage Or Course List """
	search = request.POST.get('search');
	data = {}
	# if No value return Tranding Result
	data['result'] = {}
	if len(search) == 0:
		topics = {1:'Tranding Search'}
		data['index'] = topics
		trandingSearch = ['Engineering','Business & Management Studies','MBA/PGDM','IT & Software','Science','design','Medicine & Health Sciences','Hospitality & Travel']
		data['result'].update({1:trandingSearch})
	else:
		topics = {1:'course',2:'Collage /University'}
		data['index'] = topics
		courseList = ['Business & Management Studies','IT & Software', 
		'Electronics & Communication Engineering','Business & Management Studies','BE/ B.Tech','B.SC.','BBA',
		'Computer Science Engineering','Civil Engineering','Electronics & Communication Engineering','Accounting & Commerce',
		'Accounting & Commerce']

		collageList = ['AIIMS','NIT RAIPUR','IIT DELHI','IIT Bombay','NIT Trichy','NIT Warangal','MNIT JAIPUR','IIIT Allahabad'
		'as']

		data['result'].update({1: list(np.array(list(set(process.extract(search, courseList, limit=5))))[:,0])  }) 
		data['result'].update({2: list(np.array(list(set(process.extract(search, collageList,limit=5))))[:,0]) })

	return HttpResponse(json.dumps(data), content_type='application/json')

def getCareerList(request):
	"""Return top Collage Or Course List """
	search = request.POST.get('search');
	data = {}
	# if No value return Tranding Result
	data['result'] = {}
	if len(search) == 0:
		topics = {1:'Tranding Search'}
		data['index'] = topics
		trandingSearch = ['Engineering','Computer Engineer','Software Engineer','Teacher','Doctor','Pilot','Charted Accountant']
		data['result'].update({1:trandingSearch})
	else:
		topics = {1:'Career'}
		careerList = ["Actor","Anthropologist","Architect","Actuary","Animation","Astronomer","Auctioneer","Astronauts","Accountant","Radio and TV anchor","Accessory Designer",
		"Advertising Executive","Aeronautical Engineer","Aerospace Engineer","Agricultural Scientist","Air Hostess","TV Anchor","Archaeologist/ Historian","Army Officer","Financial Analyst",
		"Chartered Accountant","Commercial Artist","Insurance Agent","Travel Agent","Agricultural Engineer","Animal Trainer","Ayurvedic Doctor","Cost Accountant","Credit Analyst","Database Administrator","Equity Analyst","Business Analysts",
		"Ceramic Artists","Automotive Designer","BPO Associate","System Analyst","Aerobic Instructors and Fitness Trainers","Air Force Officer","Aircraft Maintenance Engineer","Product and Industrial Design","Air Traffic Control Officer",
		"Audio Recording Engineers","Umpires and Referees","Medical &amp; Technical Illustrators","Mobile App Designer","Mobile App Developer","Big Data Analyst"]
		numpyResult = list(set(process.extract(search, careerList, limit=5)))
		sortedResult = sorted(numpyResult, key=lambda inputProcess: inputProcess[1], reverse=True)
		data['result'].update({ 1: list(np.array(sortedResult)[:,0]) }) 

	return HttpResponse(json.dumps(data), content_type='application/json')


def getExamList(request):
	"""Return top Collage Or Course List """
	search = request.POST.get('search');
	data = {}
	# if No value return Tranding Result
	data['result'] = {}
	if len(search) == 0:
		topics = {1:'Tranding Search'}
		data['index'] = topics
		trandingSearch = ['JEE Mains','CAT','MAT','GATE','CMAT','NEET UG','IIT JAM']
		data['result'].update({ 1: trandingSearch })
	else:
		topics = {1:'Career'}
		examList = ["ACLAT", "ANUPGCET", "AICET", "Alliance AUEET", "Amity JEE", "AISEEE", "Business & Management Studies Exams", "MBA / PGDM Exams", "AJEE", "AIFD WAT", "Teaching & Education Exams", "BBA Exams", "Hospitality & Travel Exams", "Medicine & Health Sciences Exams", "IT & Software Exams", "Humanities & Social Sciences Exams"]
		data['result'].update({ 1: [s for s in examList if search.lower() in s.lower()] }) 
	return HttpResponse(json.dumps(data), content_type='application/json')