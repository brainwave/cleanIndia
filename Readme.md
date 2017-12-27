# Clean India (Swachh Bharat/स्वच्छ भारत )

While driving on the mountain sides in Dehra, you will be mesmerized by the natural beauty of the hillsides, until you notice the garbage strewn on the side of the road. Endless pieces of plastics, glass and sometimes metal - just strewn all over. Humans are never going to clean it because it costs to do that, and its risky on the mountain sides. 

This project is an attempt at automating the process. A solar powered robot that can clean the mountain sides, bit by bit, by picking up trash would slowly but surely be able to clean a respectable amount of terrain in an environment friendly manner. It also wont endanger human or animal life. 

## Challenges 
There are few distinct areas to be worked upon before this trash picking land scape cleaning robot can come to life. These are

- Trash Recognition : It needs to spot trash on all kinds of terrains - road to rivers, lush green lands to barren rocky patches. Most imporantly, it needs to be able to tell biodegradable trash from non-biodegradable trash, and only bother about the latter. This is because in actual operation, this robot is likely to be slow and constrained by available energy. Saving resources would be crucial.
- Terrain Recognition : It also needs to be able to tell the safe terrains from unsafe ones. It needs to avoid oncoming vehicles, trees, animals, high gradients, slippery/wet land, water bodies, rocky/gravel land, etc.
- Navigation : While avoiding obstacles, static or moving, it needs to reach the point where trash is present and collect it. I'm thinking SLAM might be ideal here, but I'll be exploring path planners such as A* first.
- Communication systems
- Energy Systems
- Radar/IR systems for night time (slow robot needs to work all the time)
- Mechanical design - Obviously an ATV but rocker bogie like Mars Rovers might be too slow. Maybe tensegrity structures? :o
- Mechanical Design - trash picking mechanism, storing mechanism
- Power systems - charging, estimation, power saving tech, appropriate actions (Cool mini water turbine so it can charge itself from streams or wind muhahaha) 

### Other concerns
- Trash digestion systems
- Backup energy source/options

## Status
Alpha Draft Stage.

I'm learning the technologies involved.

Currently I am working on the problem of trash recognition. The terrains are vastly different, from road side to rivers, from lush green lands to barren, rocky patches. The robot needs to identify all these terrains, spot different kinds of trash in these terrain, navigate its way through, then clean it.

### 28 Dec 2017
SVM implementation in python
Trained on TrashNET database
Not very good results. Confuses common things like glass/plastics and paper/cardboard. Not even geared to determine trash vs non-trash, need lot of negative samples.
I should probably download the 3.5gb original dataset and examine if it has new content.

# But, why?
The gargantuan attempt at making India cleaner is commendable. Effectiveness aside, a cleaner India is a very necessary goal.
