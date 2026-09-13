# -*- coding: utf-8 -*-
"""Faculty directories + highlighted AI/CS advisors for the admissions portal."""

# Official faculty / research-area directories keyed by school short name used in programs.
FACULTY_DIRS = {
    # Hong Kong
    "HKU": {
        "all": "https://www.cs.hku.hk/people/academic-staff",
        "ai": "https://ai.hku.hk/people/academic-staff",
        "note": "CDS：CS Division + AI & Data Science Division",
    },
    "CUHK": {
        "all": "https://www.cse.cuhk.edu.hk/people/faculty/",
        "ai": "https://www.cse.cuhk.edu.hk/people/faculty/",
        "note": "CSE faculty page；可按 Artificial Intelligence 等标签筛选",
    },
    "HKUST": {
        "all": "https://cse.hkust.edu.hk/admin/people/faculty/",
        "ai": "https://cse.hkust.edu.hk/admin/people/faculty/",
        "note": "CSE faculty；多位标注 Artificial Intelligence / Vision",
    },
    "CityUHK": {
        "all": "https://www.cs.cityu.edu.hk/people/academic-staff",
        "ai": "https://www.cs.cityu.edu.hk/research",
        "note": "CS 学术人员 + 研究组",
    },
    "PolyU": {
        "all": "https://www.polyu.edu.hk/comp/people/academic-staff/",
        "ai": "https://www.polyu.edu.hk/comp/research/",
        "note": "Computing 学术人员",
    },
    "HKBU": {
        "all": "https://www.comp.hkbu.edu.hk/v1/?page=people",
        "ai": "https://www.comp.hkbu.edu.hk/v1/?page=people",
        "note": "COMP people",
    },
    "HKUST(GZ)": {
        "all": "https://facultyprofiles.hkust-gz.edu.cn/",
        "ai": "https://hkust-gz.edu.cn/academics/four-hubs",
        "note": "按 Hub/Thrust 浏览导师",
    },
    "CUHK-Shenzhen": {
        "all": "https://sse.cuhk.edu.cn/en/faculty",
        "ai": "https://sse-mphil-phd.cuhk.edu.cn/en/program/CIE",
        "note": "SSE faculty；另见 SDS",
    },
    "CUHK-Shenzhen SDS": {
        "all": "https://sds.cuhk.edu.cn/en/teacher",
        "ai": "https://sds.cuhk.edu.cn/en/teacher",
        "note": "School of Data Science faculty",
    },
    "CityUHK (Dongguan)": {
        "all": "https://www.cityu-dg.edu.cn/en/home",
        "ai": "https://pga.cityu-dg.edu.cn/en/home",
        "note": "新校区；师资名单以官网更新为准",
    },
    "BNBU/UIC": {
        "all": "https://gs.bnbu.edu.cn/graduate1/Research_Postgraduate_Programme/Computer_Science_and_Technology/SUPERVISORS.htm",
        "ai": "https://gs.bnbu.edu.cn/graduate1/Research_Postgraduate_Programme/Computer_Science_and_Technology.htm",
        "note": "CS&T 导师名单",
    },
    # Singapore
    "NUS": {
        "all": "https://www.comp.nus.edu.sg/about/faculty/",
        "ai": "https://www.comp.nus.edu.sg/cs/research/ai/people/",
        "note": "SoC faculty + AI research people；另见 NUS AI Lab",
    },
    "NTU": {
        "all": "https://www.ntu.edu.sg/computing/our-faculty/faculty-at-ccds",
        "ai": "https://www.ntu.edu.sg/computing/ai-at-ntu/ai-faculty",
        "note": "CCDS 全员目录 + AI Faculty 专题",
    },
    "SMU": {
        "all": "https://computing.smu.edu.sg/faculty",
        "ai": "https://computing.smu.edu.sg/faculty",
        "note": "SCIS faculty",
    },
    "SUTD": {
        "all": "https://www.sutd.edu.sg/education/faculty/",
        "ai": "https://istd.sutd.edu.sg/people/faculty",
        "note": "ISTD 等 pillar faculty",
    },
    "SIT": {
        "all": "https://www.singaporetech.edu.sg/about/our-people",
        "ai": "https://www.singaporetech.edu.sg/graduate",
        "note": "SIT people / graduate supervisors",
    },
    "SINGA": {
        "all": "https://www.a-star.edu.sg/Scholarships/for-graduate-studies/singapore-international-graduate-award-singa",
        "ai": "https://www.a-star.edu.sg/Research",
        "note": "通过 SINGA 选 A*STAR / 大学导师",
    },
    # United States (CS / EECS directories)
    "CMU": {
        "all": "https://csd.cs.cmu.edu/people/faculty",
        "ai": "https://www.cs.cmu.edu/research/ai",
        "note": "CSD faculty；SCS 还有 ML/RI/LTI 等系",
    },
    "MIT": {
        "all": "https://www.eecs.mit.edu/role/faculty/",
        "ai": "https://www.eecs.mit.edu/role/faculty-aid/",
        "note": "EECS faculty；另有 Faculty AI+D / CS / EE",
    },
    "Stanford": {
        "all": "https://www.cs.stanford.edu/people/faculty",
        "ai": "https://hai.stanford.edu/people",
        "note": "CS faculty + Stanford HAI",
    },
    "UC Berkeley": {
        "all": "https://www2.eecs.berkeley.edu/Faculty/Lists/list.html",
        "ai": "https://www2.eecs.berkeley.edu/Research/Areas/AI/",
        "note": "EECS faculty by research area",
    },
    "UIUC": {
        "all": "https://siebelschool.illinois.edu/about/people/faculty",
        "ai": "https://siebelschool.illinois.edu/research/areas",
        "note": "Siebel School faculty",
    },
    "Princeton": {
        "all": "https://www.cs.princeton.edu/people/faculty",
        "ai": "https://www.cs.princeton.edu/research",
        "note": "CS faculty",
    },
    "Cornell": {
        "all": "https://www.cs.cornell.edu/people/faculty",
        "ai": "https://www.cs.cornell.edu/research",
        "note": "CS faculty",
    },
    "Georgia Tech": {
        "all": "https://www.cc.gatech.edu/people/faculty",
        "ai": "https://www.cc.gatech.edu/research",
        "note": "College of Computing faculty",
    },
    "UW": {
        "all": "https://www.cs.washington.edu/people/faculty",
        "ai": "https://www.cs.washington.edu/research",
        "note": "CSE faculty",
    },
    "UT Austin": {
        "all": "https://www.cs.utexas.edu/people/faculty-researchers",
        "ai": "https://www.cs.utexas.edu/research",
        "note": "CS faculty",
    },
    "Caltech": {
        "all": "https://www.cms.caltech.edu/people",
        "ai": "https://www.cms.caltech.edu/research",
        "note": "CMS faculty",
    },
    "Harvard": {
        "all": "https://www.seas.harvard.edu/computer-science/people",
        "ai": "https://www.seas.harvard.edu/computer-science/research",
        "note": "SEAS CS people",
    },
    "UCSD": {
        "all": "https://cse.ucsd.edu/people/faculty",
        "ai": "https://cse.ucsd.edu/research",
        "note": "CSE faculty",
    },
    "UMich": {
        "all": "https://cse.engin.umich.edu/people/faculty/",
        "ai": "https://cse.engin.umich.edu/research/",
        "note": "CSE faculty",
    },
    "UCLA": {
        "all": "https://www.cs.ucla.edu/people/faculty/",
        "ai": "https://www.cs.ucla.edu/research/",
        "note": "CS faculty",
    },
    "Columbia": {
        "all": "https://www.cs.columbia.edu/people/faculty/",
        "ai": "https://www.cs.columbia.edu/research/",
        "note": "CS faculty",
    },
    "JHU": {
        "all": "https://www.cs.jhu.edu/faculty/",
        "ai": "https://www.cs.jhu.edu/research/",
        "note": "CS faculty",
    },
    "Purdue": {
        "all": "https://www.cs.purdue.edu/people/faculty/index.html",
        "ai": "https://www.cs.purdue.edu/research/index.html",
        "note": "CS faculty",
    },
    "UMD": {
        "all": "https://www.cs.umd.edu/people/faculty",
        "ai": "https://www.cs.umd.edu/research",
        "note": "CS faculty",
    },
    "UPenn": {
        "all": "https://www.cis.upenn.edu/people/faculty/",
        "ai": "https://www.cis.upenn.edu/research/",
        "note": "CIS faculty",
    },
    "USC": {
        "all": "https://www.cs.usc.edu/faculty-staff/",
        "ai": "https://www.cs.usc.edu/research/",
        "note": "CS faculty",
    },
    "UW–Madison": {
        "all": "https://www.cs.wisc.edu/people/faculty/",
        "ai": "https://www.cs.wisc.edu/research/",
        "note": "CS faculty",
    },
    "Yale": {
        "all": "https://cpsc.yale.edu/people/faculty",
        "ai": "https://cpsc.yale.edu/research",
        "note": "CPSC faculty",
    },
    "Duke": {
        "all": "https://www.cs.duke.edu/people/faculty",
        "ai": "https://www.cs.duke.edu/research",
        "note": "CS faculty",
    },
    "Brown": {
        "all": "https://cs.brown.edu/people/faculty/",
        "ai": "https://cs.brown.edu/research/",
        "note": "CS faculty",
    },
    "UChicago": {
        "all": "https://cs.uchicago.edu/people/faculty/",
        "ai": "https://cs.uchicago.edu/research/",
        "note": "CS faculty",
    },
    "UCI": {
        "all": "https://www.ics.uci.edu/faculty/",
        "ai": "https://www.ics.uci.edu/research/",
        "note": "ICS faculty",
    },
    "Virginia Tech": {
        "all": "https://cs.vt.edu/People/Faculty.html",
        "ai": "https://cs.vt.edu/Research.html",
        "note": "CS faculty",
    },
    "NYU": {
        "all": "https://cs.nyu.edu/home/people/faculty.html",
        "ai": "https://cs.nyu.edu/home/research/",
        "note": "Courant CS faculty",
    },
    "Northwestern": {
        "all": "https://www.mccormick.northwestern.edu/computer-science/people/faculty/",
        "ai": "https://www.mccormick.northwestern.edu/computer-science/research/",
        "note": "CS faculty",
    },
    "Rice": {
        "all": "https://csweb.rice.edu/people/faculty",
        "ai": "https://csweb.rice.edu/research",
        "note": "CS faculty",
    },
    "CU Boulder": {
        "all": "https://www.colorado.edu/cs/people/faculty",
        "ai": "https://www.colorado.edu/cs/research",
        "note": "CS faculty",
    },
    "UNC": {
        "all": "https://cs.unc.edu/people/faculty/",
        "ai": "https://cs.unc.edu/research/",
        "note": "CS faculty",
    },
    "Northeastern": {
        "all": "https://www.khoury.northeastern.edu/people/faculty/",
        "ai": "https://www.khoury.northeastern.edu/research/",
        "note": "Khoury faculty",
    },
    "UC Davis": {
        "all": "https://cs.ucdavis.edu/people/faculty",
        "ai": "https://cs.ucdavis.edu/research",
        "note": "CS faculty",
    },
    "UCSB": {
        "all": "https://www.cs.ucsb.edu/people/faculty",
        "ai": "https://www.cs.ucsb.edu/research",
        "note": "CS faculty",
    },
    "UMass": {
        "all": "https://www.cics.umass.edu/people/faculty",
        "ai": "https://www.cics.umass.edu/research",
        "note": "CICS faculty",
    },
    "Dartmouth": {
        "all": "https://web.cs.dartmouth.edu/people",
        "ai": "https://web.cs.dartmouth.edu/research",
        "note": "CS people",
    },
    "Ohio State": {
        "all": "https://cse.osu.edu/people",
        "ai": "https://cse.osu.edu/research",
        "note": "CSE people",
    },
    "Penn State": {
        "all": "https://www.eecs.psu.edu/departments/listCSfaculty.aspx",
        "ai": "https://www.eecs.psu.edu/research/",
        "note": "EECS CS faculty",
    },
    "UMN": {
        "all": "https://cse.umn.edu/cs/faculty",
        "ai": "https://cse.umn.edu/cs/research",
        "note": "CS faculty",
    },
    "UVA": {
        "all": "https://engineering.virginia.edu/departments/computer-science/people",
        "ai": "https://engineering.virginia.edu/departments/computer-science/research",
        "note": "CS people",
    },
    "Vanderbilt": {
        "all": "https://engineering.vanderbilt.edu/academics/departments/computer-science/people/",
        "ai": "https://engineering.vanderbilt.edu/academics/departments/computer-science/",
        "note": "CS people",
    },
    "ASU": {
        "all": "https://search.asu.edu/profile/faculty?dept=Computer%20Science",
        "ai": "https://scai.engineering.asu.edu/",
        "note": "SCAI / CS faculty",
    },
    "Texas A&M": {
        "all": "https://engineering.tamu.edu/cse/people/faculty.html",
        "ai": "https://engineering.tamu.edu/cse/research/index.html",
        "note": "CSE faculty",
    },
    "Rutgers": {
        "all": "https://www.cs.rutgers.edu/people/professors",
        "ai": "https://www.cs.rutgers.edu/research",
        "note": "CS professors",
    },
    "Stony Brook": {
        "all": "https://www.cs.stonybrook.edu/people/faculty",
        "ai": "https://www.cs.stonybrook.edu/research",
        "note": "CS faculty",
    },
    "UUtah": {
        "all": "https://www.cs.utah.edu/people/faculty/",
        "ai": "https://www.cs.utah.edu/research/",
        "note": "CS faculty",
    },
    "WashU": {
        "all": "https://cse.wustl.edu/faculty-research/faculty.html",
        "ai": "https://cse.wustl.edu/research/index.html",
        "note": "CSE faculty",
    },
    "NCSU": {
        "all": "https://www.csc.ncsu.edu/people/",
        "ai": "https://www.csc.ncsu.edu/research/",
        "note": "CSC people",
    },
    "Notre Dame": {
        "all": "https://cse.nd.edu/faculty/",
        "ai": "https://cse.nd.edu/research/",
        "note": "CSE faculty",
    },
    "Rochester": {
        "all": "https://www.cs.rochester.edu/people/faculty/",
        "ai": "https://www.cs.rochester.edu/research/",
        "note": "CS faculty",
    },
    "UFlorida": {
        "all": "https://www.cise.ufl.edu/people/faculty/",
        "ai": "https://www.cise.ufl.edu/research/",
        "note": "CISE faculty",
    },
    "BU": {
        "all": "https://www.bu.edu/cs/people/faculty/",
        "ai": "https://www.bu.edu/cs/research/",
        "note": "CS faculty",
    },
    "IU": {
        "all": "https://cs.indiana.edu/people/faculty/",
        "ai": "https://cs.indiana.edu/research/",
        "note": "Luddy CS faculty",
    },
    "Iowa State": {
        "all": "https://www.cs.iastate.edu/people/faculty",
        "ai": "https://www.cs.iastate.edu/research",
        "note": "CS faculty",
    },
    "Oregon State": {
        "all": "https://eecs.oregonstate.edu/people/faculty",
        "ai": "https://eecs.oregonstate.edu/research",
        "note": "EECS faculty",
    },
    "UCSC": {
        "all": "https://engineering.ucsc.edu/departments/computer-science-and-engineering/people/",
        "ai": "https://engineering.ucsc.edu/research/",
        "note": "CSE people",
    },
    "UCR": {
        "all": "https://www1.cs.ucr.edu/people/faculty",
        "ai": "https://www1.cs.ucr.edu/research",
        "note": "CS faculty",
    },
    "UIC": {
        "all": "https://cs.uic.edu/people/faculty/",
        "ai": "https://cs.uic.edu/research/",
        "note": "UIC CS faculty",
    },
    "UCF": {
        "all": "https://www.cs.ucf.edu/people/faculty/",
        "ai": "https://www.cs.ucf.edu/research/",
        "note": "CS faculty",
    },
    "Buffalo": {
        "all": "https://engineering.buffalo.edu/computer-science-engineering/people/faculty-directory.html",
        "ai": "https://engineering.buffalo.edu/computer-science-engineering/research.html",
        "note": "CSE faculty",
    },
    "MSU": {
        "all": "https://www.cse.msu.edu/People/Faculty/",
        "ai": "https://www.cse.msu.edu/Research/",
        "note": "CSE faculty",
    },
    "Pitt": {
        "all": "https://www.cs.pitt.edu/people/faculty",
        "ai": "https://www.cs.pitt.edu/research",
        "note": "CS faculty",
    },
    "UArizona": {
        "all": "https://www.cs.arizona.edu/people/faculty",
        "ai": "https://www.cs.arizona.edu/research",
        "note": "CS faculty",
    },
    "GMU": {
        "all": "https://cs.gmu.edu/people/faculty/",
        "ai": "https://cs.gmu.edu/research/",
        "note": "CS faculty",
    },
    "UT Dallas": {
        "all": "https://cs.utdallas.edu/people/faculty/",
        "ai": "https://cs.utdallas.edu/research/",
        "note": "CS faculty",
    },
    "Tufts": {
        "all": "https://engineering.tufts.edu/cs/people/faculty",
        "ai": "https://engineering.tufts.edu/cs/research",
        "note": "CS faculty",
    },
    "RPI": {
        "all": "https://science.rpi.edu/computer-science/faculty",
        "ai": "https://science.rpi.edu/computer-science/research",
        "note": "CS faculty",
    },
    "Case Western": {
        "all": "https://engineering.case.edu/computer-and-data-sciences/people",
        "ai": "https://engineering.case.edu/computer-and-data-sciences/research",
        "note": "CDS people",
    },
    "UMBC": {
        "all": "https://www.csee.umbc.edu/people/faculty/",
        "ai": "https://www.csee.umbc.edu/research/",
        "note": "CSEE faculty",
    },
    "Stevens": {
        "all": "https://www.stevens.edu/school-of-engineering-and-science/departments/computer-science/faculty",
        "ai": "https://www.stevens.edu/school-of-engineering-and-science/departments/computer-science",
        "note": "CS faculty",
    },
    "UDelaware": {
        "all": "https://www.cis.udel.edu/people/faculty/",
        "ai": "https://www.cis.udel.edu/research/",
        "note": "CIS faculty",
    },
    "UNebraska": {
        "all": "https://computing.unl.edu/faculty/",
        "ai": "https://computing.unl.edu/research/",
        "note": "Computing faculty",
    },
    "FSU": {
        "all": "https://www.cs.fsu.edu/department/faculty/",
        "ai": "https://www.cs.fsu.edu/research/",
        "note": "CS faculty",
    },
    "Syracuse": {
        "all": "https://ecs.syracuse.edu/faculty-staff",
        "ai": "https://ecs.syracuse.edu/academics/computer-science",
        "note": "ECS faculty/staff",
    },
    "WSU": {
        "all": "https://school.eecs.wsu.edu/people/faculty/",
        "ai": "https://school.eecs.wsu.edu/research/",
        "note": "EECS faculty",
    },
    "Clemson": {
        "all": "https://www.clemson.edu/cecas/departments/computing/people/faculty.html",
        "ai": "https://www.clemson.edu/cecas/departments/computing/research/",
        "note": "Computing faculty",
    },
    "Drexel": {
        "all": "https://drexel.edu/cci/about/directory/",
        "ai": "https://drexel.edu/cci/research/",
        "note": "CCI directory",
    },
    "UConn": {
        "all": "https://www.cse.uconn.edu/people/faculty/",
        "ai": "https://www.cse.uconn.edu/research/",
        "note": "CSE faculty",
    },
    "TTIC": {
        "all": "https://www.ttic.edu/faculty/",
        "ai": "https://www.ttic.edu/research/",
        "note": "TTIC faculty",
    },
    "UNC Charlotte": {
        "all": "https://cci.charlotte.edu/directory/",
        "ai": "https://cci.charlotte.edu/research/",
        "note": "CCI directory",
    },
    "UT Arlington": {
        "all": "https://www.uta.edu/academics/schools-colleges/engineering/academics/departments/cse/faculty",
        "ai": "https://www.uta.edu/academics/schools-colleges/engineering/academics/departments/cse/research",
        "note": "CSE faculty",
    },
    "UIowa": {
        "all": "https://cs.uiowa.edu/people/faculty",
        "ai": "https://cs.uiowa.edu/research",
        "note": "CS faculty",
    },
    "Georgetown": {
        "all": "https://cs.georgetown.edu/people/faculty/",
        "ai": "https://cs.georgetown.edu/research/",
        "note": "CS faculty",
    },
    "GWU": {
        "all": "https://www.cs.seas.gwu.edu/faculty",
        "ai": "https://www.cs.seas.gwu.edu/research",
        "note": "CS faculty",
    },
    "Binghamton": {
        "all": "https://www.binghamton.edu/computer-science/people/index.html",
        "ai": "https://www.binghamton.edu/computer-science/research/index.html",
        "note": "CS people",
    },
    "NJIT": {
        "all": "https://computing.njit.edu/people",
        "ai": "https://computing.njit.edu/research",
        "note": "Computing people",
    },
    "WPI": {
        "all": "https://www.wpi.edu/academics/departments/computer-science/faculty-staff",
        "ai": "https://www.wpi.edu/academics/departments/computer-science/research",
        "note": "CS faculty/staff",
    },
    "UTK": {
        "all": "https://www.eecs.utk.edu/people/",
        "ai": "https://www.eecs.utk.edu/research/",
        "note": "EECS people",
    },
    "Emory": {
        "all": "https://www.cs.emory.edu/people/faculty/",
        "ai": "https://www.cs.emory.edu/research/",
        "note": "CS faculty",
    },
    "UGA": {
        "all": "https://www.cs.uga.edu/directory/faculty",
        "ai": "https://www.cs.uga.edu/research",
        "note": "CS faculty",
    },
    "Temple": {
        "all": "https://cis.temple.edu/people/faculty",
        "ai": "https://cis.temple.edu/research",
        "note": "CIS faculty",
    },
    "Lehigh": {
        "all": "https://engineering.lehigh.edu/cse/faculty",
        "ai": "https://engineering.lehigh.edu/cse/research",
        "note": "CSE faculty",
    },
    "IIT": {
        "all": "https://www.iit.edu/computer-science/faculty",
        "ai": "https://www.iit.edu/computer-science/research",
        "note": "CS faculty",
    },
    "Auburn": {
        "all": "https://www.eng.auburn.edu/comp/faculty/",
        "ai": "https://www.eng.auburn.edu/comp/research/",
        "note": "CSSE faculty",
    },
    "UH": {
        "all": "https://www.cs.uh.edu/people/faculty/",
        "ai": "https://www.cs.uh.edu/research/",
        "note": "CS faculty",
    },
    "Colorado Mines": {
        "all": "https://cs.mines.edu/people/",
        "ai": "https://cs.mines.edu/research/",
        "note": "CS people",
    },
}

# Highlighted AI / ML / CV / NLP / robotics advisors (not exhaustive).
# home = personal homepage when known; profile = department profile page.
FACULTY_HIGHLIGHTS = [
    # HKU
    {"school": "HKU", "name": "Yi Ma", "title": "Chair of AI / Director of CDS", "areas": "AI, representation learning, data science", "home": "https://people.eecs.berkeley.edu/~yima/", "profile": "https://ai.hku.hk/people/academic-staff"},
    {"school": "HKU", "name": "Ping Luo", "title": "Professor", "areas": "Computer vision, generative AI, multimodal learning", "home": "http://luoping.me/", "profile": "https://ai.hku.hk/people/academic-staff"},
    {"school": "HKU", "name": "Reynold Cheng", "title": "Professor / Division Head (AI & DS)", "areas": "Data science, big data, databases", "home": "https://www.cs.hku.hk/~ckcheng/", "profile": "https://ai.hku.hk/people/academic-staff"},
    {"school": "HKU", "name": "Chao Huang", "title": "Assistant Professor", "areas": "Recommender systems, graph ML, data mining", "home": "https://sites.google.com/view/chaoh", "profile": "https://ai.hku.hk/people/academic-staff"},
    {"school": "HKU", "name": "Difan Zou", "title": "Assistant Professor", "areas": "ML theory, optimization, deep learning", "home": "https://difanzou.github.io/", "profile": "https://ai.hku.hk/people/academic-staff"},
    # CUHK
    {"school": "CUHK", "name": "Irwin King", "title": "Professor", "areas": "Machine learning, social computing, AI", "home": "https://www.cse.cuhk.edu.hk/~king/", "profile": "https://www.cse.cuhk.edu.hk/people/faculty/"},
    {"school": "CUHK", "name": "Yu Cheng", "title": "Professor", "areas": "Machine learning, trustworthy AI, NLP", "home": "https://www.cse.cuhk.edu.hk/~ycheng/", "profile": "https://www.cse.cuhk.edu.hk/people/faculty/"},
    {"school": "CUHK", "name": "Qi Dou", "title": "Associate Professor", "areas": "Medical AI, computer vision, robotics", "home": "https://www.cse.cuhk.edu.hk/~qdou/", "profile": "https://www.cse.cuhk.edu.hk/people/faculty/"},
    {"school": "CUHK", "name": "Weiyang Liu", "title": "Assistant Professor", "areas": "Generative AI, foundation models, LLMs, CV", "home": "https://wyliu.com/", "profile": "https://www.cse.cuhk.edu.hk/people/faculty/"},
    {"school": "CUHK", "name": "Pheng Ann Heng", "title": "Professor", "areas": "Medical imaging, VR/AR, AI for medicine", "home": "https://www.cse.cuhk.edu.hk/~pheng/", "profile": "https://www.cse.cuhk.edu.hk/people/faculty/"},
    {"school": "CUHK", "name": "Sinno Jialin Pan", "title": "Professor", "areas": "Transfer learning, machine learning", "home": "https://www.cse.cuhk.edu.hk/~sinnopan/", "profile": "https://www.cse.cuhk.edu.hk/people/faculty/"},
    # HKUST
    {"school": "HKUST", "name": "Song Guo", "title": "Chair Professor", "areas": "AI systems, edge AI, networking", "home": "https://cse.hkust.edu.hk/~songguo/", "profile": "https://cse.hkust.edu.hk/admin/people/faculty/"},
    {"school": "HKUST", "name": "Jiaya Jia", "title": "Chair Professor", "areas": "Computer vision, generative AI, graphics", "home": "https://jiaya.me/", "profile": "https://cse.hkust.edu.hk/admin/people/faculty/"},
    {"school": "HKUST", "name": "James Kwok", "title": "Professor", "areas": "Machine learning, kernel methods, deep learning", "home": "https://cse.hkust.edu.hk/~jamesk/", "profile": "https://cse.hkust.edu.hk/admin/people/faculty/"},
    {"school": "HKUST", "name": "Qifeng Chen", "title": "Associate Professor", "areas": "Computer vision, computational photography, AI", "home": "https://cqf.io/", "profile": "https://cse.hkust.edu.hk/admin/people/faculty/"},
    {"school": "HKUST", "name": "Yangqiu Song", "title": "Associate Professor", "areas": "Knowledge graph, NLP, data mining", "home": "https://www.cse.ust.hk/~yqsong/", "profile": "https://cse.hkust.edu.hk/admin/people/faculty/"},
    {"school": "HKUST", "name": "Junxian He", "title": "Assistant Professor", "areas": "NLP, LLMs, AI", "home": "https://jxhe.github.io/", "profile": "https://cse.hkust.edu.hk/admin/people/faculty/"},
    {"school": "HKUST", "name": "Hao Chen", "title": "Assistant Professor", "areas": "Medical image analysis, computer vision", "home": "https://cse.hkust.edu.hk/~jhc/", "profile": "https://cse.hkust.edu.hk/admin/people/faculty/"},
    {"school": "HKUST", "name": "Nevin Zhang", "title": "Professor", "areas": "Bayesian networks, probabilistic graphical models", "home": "https://cse.hkust.edu.hk/~lzhang/", "profile": "https://cse.hkust.edu.hk/admin/people/faculty/"},
    # NUS
    {"school": "NUS", "name": "David Hsu", "title": "Professor", "areas": "Robotics, AI planning, decision making", "home": "https://www.comp.nus.edu.sg/~dyhsu/", "profile": "https://www.comp.nus.edu.sg/cs/research/ai/people/"},
    {"school": "NUS", "name": "Wee Sun Lee", "title": "Professor", "areas": "Machine learning, AI", "home": "https://www.comp.nus.edu.sg/~leews/", "profile": "https://www.comp.nus.edu.sg/cs/research/ai/people/"},
    {"school": "NUS", "name": "Min-Yen Kan", "title": "Associate Professor", "areas": "NLP, information retrieval, digital libraries", "home": "https://www.comp.nus.edu.sg/~kanmy/", "profile": "https://www.comp.nus.edu.sg/cs/research/ai/people/"},
    {"school": "NUS", "name": "Hwee Tou Ng", "title": "Professor", "areas": "NLP, machine translation", "home": "https://www.comp.nus.edu.sg/~nght/", "profile": "https://www.comp.nus.edu.sg/cs/research/ai/people/"},
    {"school": "NUS", "name": "Angela Yao", "title": "Associate Professor", "areas": "Computer vision, human activity understanding", "home": "https://www.comp.nus.edu.sg/~ayao/", "profile": "https://www.comp.nus.edu.sg/about/faculty/"},
    # NTU
    {"school": "NTU", "name": "Bo An", "title": "Professor / Head of AI Division", "areas": "Multi-agent systems, AI, decision making", "home": "https://personal.ntu.edu.sg/boan/", "profile": "https://www.ntu.edu.sg/computing/ai-at-ntu/ai-faculty"},
    {"school": "NTU", "name": "Erik Cambria", "title": "Professor", "areas": "Sentiment analysis, NLP, affective computing", "home": "https://www.sentic.net/", "profile": "https://www.ntu.edu.sg/computing/ai-at-ntu/ai-faculty"},
    {"school": "NTU", "name": "Guan Cuntai", "title": "President's Chair in AI", "areas": "Brain-computer interface, AI for health", "home": "https://dr.ntu.edu.sg/entities/person/Cuntai-Guan", "profile": "https://www.ntu.edu.sg/computing/ai-at-ntu/ai-faculty"},
    {"school": "NTU", "name": "Zhang Jie", "title": "Professor", "areas": "Computational intelligence, trust, recommender systems", "home": "https://personal.ntu.edu.sg/zhangj/", "profile": "https://www.ntu.edu.sg/computing/ai-at-ntu/ai-faculty"},
    {"school": "NTU", "name": "Han Yu", "title": "Associate Professor", "areas": "Federated learning, trustworthy AI, HCI", "home": "https://personal.ntu.edu.sg/han.yu/", "profile": "https://www.ntu.edu.sg/computing/ai-at-ntu/ai-faculty"},
    # SMU / SUTD
    {"school": "SMU", "name": "Pradeep Varakantham", "title": "Professor", "areas": "AI, sequential decision making, human-AI collaboration", "home": "https://faculty.smu.edu.sg/profile/pradeep-varakantham-1646", "profile": "https://computing.smu.edu.sg/faculty"},
    {"school": "SUTD", "name": "ISTD Faculty", "title": "Pillar faculty list", "areas": "AI, data science, interactive design, security", "home": "https://istd.sutd.edu.sg/people/faculty", "profile": "https://istd.sutd.edu.sg/people/faculty"},
    # Top US (representative AI advisors)
    {"school": "MIT", "name": "EECS Faculty AI+D", "title": "Faculty directory (AI+D)", "areas": "AI + Decision-making track faculty list", "home": "https://www.eecs.mit.edu/role/faculty-aid/", "profile": "https://www.eecs.mit.edu/role/faculty/"},
    {"school": "MIT", "name": "CSAIL People", "title": "Lab directory", "areas": "AI, systems, theory across CSAIL", "home": "https://www.csail.mit.edu/people", "profile": "https://www.csail.mit.edu/people"},
    {"school": "Stanford", "name": "Chelsea Finn", "title": "Assistant Professor", "areas": "Robot learning, meta-learning, RL", "home": "https://ai.stanford.edu/~cbfinn/", "profile": "https://www.cs.stanford.edu/people/faculty"},
    {"school": "Stanford", "name": "Fei-Fei Li", "title": "Professor", "areas": "Computer vision, AI, HAI", "home": "https://profiles.stanford.edu/fei-fei-li", "profile": "https://www.cs.stanford.edu/people/faculty"},
    {"school": "Stanford", "name": "Percy Liang", "title": "Associate Professor", "areas": "NLP, foundation models, trustworthy ML", "home": "https://cs.stanford.edu/~pliang/", "profile": "https://www.cs.stanford.edu/people/faculty"},
    {"school": "Stanford", "name": "Chris Ré", "title": "Associate Professor", "areas": "Machine learning systems, data-centric AI", "home": "https://cs.stanford.edu/~chrismre/", "profile": "https://www.cs.stanford.edu/people/faculty"},
    {"school": "CMU", "name": "Machine Learning Department Faculty", "title": "MLD faculty list", "areas": "Core ML, deep learning, theory", "home": "https://www.ml.cmu.edu/people/faculty.html", "profile": "https://csd.cs.cmu.edu/people/faculty"},
    {"school": "CMU", "name": "RI Faculty", "title": "Robotics Institute", "areas": "Robotics, vision, autonomy", "home": "https://www.ri.cmu.edu/ri-faculty/", "profile": "https://www.ri.cmu.edu/ri-faculty/"},
    {"school": "UC Berkeley", "name": "BAIR Faculty", "title": "Berkeley AI Research", "areas": "AI, RL, vision, NLP, robotics", "home": "https://bair.berkeley.edu/people.html", "profile": "https://www2.eecs.berkeley.edu/Research/Areas/AI/"},
    {"school": "UC Berkeley", "name": "Pieter Abbeel", "title": "Professor", "areas": "Deep RL, robotics, generative models", "home": "https://people.eecs.berkeley.edu/~pabbeel/", "profile": "https://www2.eecs.berkeley.edu/Faculty/Homepages/abbeel.html"},
    {"school": "UC Berkeley", "name": "Jitendra Malik", "title": "Professor", "areas": "Computer vision", "home": "https://people.eecs.berkeley.edu/~malik/", "profile": "https://www2.eecs.berkeley.edu/Faculty/Homepages/malik.html"},
    {"school": "UIUC", "name": "Siebel Faculty", "title": "Faculty directory", "areas": "AI, systems, theory, HCI", "home": "https://siebelschool.illinois.edu/about/people/faculty", "profile": "https://siebelschool.illinois.edu/about/people/faculty"},
    {"school": "Princeton", "name": "CS Faculty", "title": "Faculty directory", "areas": "ML, theory, systems, vision", "home": "https://www.cs.princeton.edu/people/faculty", "profile": "https://www.cs.princeton.edu/people/faculty"},
    {"school": "Cornell", "name": "CS Faculty", "title": "Faculty directory", "areas": "AI, NLP, vision, systems", "home": "https://www.cs.cornell.edu/people/faculty", "profile": "https://www.cs.cornell.edu/people/faculty"},
    {"school": "Georgia Tech", "name": "ML@GT Faculty", "title": "Machine Learning Center", "areas": "Machine learning across GT", "home": "https://ml.gatech.edu/people", "profile": "https://www.cc.gatech.edu/people/faculty"},
    {"school": "UW", "name": "CSE Faculty", "title": "Faculty directory", "areas": "NLP, vision, ML, systems", "home": "https://www.cs.washington.edu/people/faculty", "profile": "https://www.cs.washington.edu/people/faculty"},
    {"school": "UT Austin", "name": "CS Faculty", "title": "Faculty directory", "areas": "AI, robotics, NLP, vision", "home": "https://www.cs.utexas.edu/people/faculty-researchers", "profile": "https://www.cs.utexas.edu/people/faculty-researchers"},
    {"school": "UMich", "name": "CSE Faculty", "title": "Faculty directory", "areas": "AI, vision, NLP, robotics", "home": "https://cse.engin.umich.edu/people/faculty/", "profile": "https://cse.engin.umich.edu/people/faculty/"},
    {"school": "UCLA", "name": "CS Faculty", "title": "Faculty directory", "areas": "AI, vision, NLP, ML", "home": "https://www.cs.ucla.edu/people/faculty/", "profile": "https://www.cs.ucla.edu/people/faculty/"},
    {"school": "Columbia", "name": "CS Faculty", "title": "Faculty directory", "areas": "ML, NLP, vision, robotics", "home": "https://www.cs.columbia.edu/people/faculty/", "profile": "https://www.cs.columbia.edu/people/faculty/"},
    {"school": "UCSD", "name": "CSE Faculty", "title": "Faculty directory", "areas": "AI, systems, theory, graphics", "home": "https://cse.ucsd.edu/people/faculty", "profile": "https://cse.ucsd.edu/people/faculty"},
]


def attach_faculty(program: dict) -> dict:
    school = program.get("school")
    d = FACULTY_DIRS.get(school)
    if d:
        program["facultyDir"] = d.get("all")
        program["facultyAiDir"] = d.get("ai")
        program["facultyNote"] = d.get("note")
    return program


def faculty_payload():
    return {
        "directories": FACULTY_DIRS,
        "highlights": FACULTY_HIGHLIGHTS,
        "disclaimer": "重点老师为 AI/ML/CV/NLP/机器人等相关代表，并非全系名单。完整名单请点各校 Faculty Directory。主页链接可能变更，以官方目录为准。",
    }
