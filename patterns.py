import random
patterns = [

			[
				[1,0,1,0,1],
				[1,0,0,0,1],
				[0,0,3,0,0],
				[0,4,4,4,0],
				[5,5,0,5,5]
			],

			[
				[1,1,1,1,1],
				[2,0,0,0,2],
				[3,0,3,0,3],
				[4,0,0,0,4],
				[5,5,5,5,5]
			],
			[
				[0,0,1,0,1],
				[1,0,2,0,0],
				[0,2,3,0,0],
				[0,4,0,4,2],
				[5,5,0,5,5]
			],
			[
				[0,0,1,0,0],
				[0,1,0,1,0],
				[0,1,1,1,0],
				[1,0,0,0,1],
				[1,0,0,0,1]
			],
			[
				[1,0,0,1,0],
				[1,0,1,0,0],
				[1,1,0,0,0],
				[1,0,1,0,0],
				[1,0,0,1,0]
			],
			[
				[1,1,1,1,1],
				[0,0,1,0,0],
				[0,0,1,0,0],
				[0,0,1,0,0],
				[1,1,1,1,1]
			],
			[
				[0,1,1,1,1],
				[0,0,0,0,0],
				[1,1,1,1,0],
				[0,0,0,0,0],
				[1,1,0,1,1]
			],
			[
				[0,1,0,1,0],
				[1,0,1,0,0],
				[0,1,1,1,1],
				[1,0,1,1,0],
				[0,0,1,0,1]
			]

]




def getpattern():
	return random.choice(patterns)







