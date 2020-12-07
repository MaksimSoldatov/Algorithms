### Sprint 1 
Task1:

The street Timofey wants to live on has length n, that is, it consists of n identical consecutive sections. On each site, either a house has already been built, or the site is empty. Timofey is looking for a place to build his house. Timofey is very sociable and does not want to live far from his acquaintances, whom he has all over the street. In order to optimally choose a place for construction, he wants to know the distance to the nearest empty lot for each lot. (For an empty area, this value will be zero - the distance to itself.)
Your task is to help Timothy calculate the required distances. For this, you have a street map. Houses in the city of Timothy were numbered in the order in which they were built, so their numbers on the map are not ordered in any way. Empty areas are indicated by zeros.

The first line contains the length of the street - n (1 ≤ n ≤ 10^6). The next line contains non-negative integers - numbers and designations of empty areas on the map (zeros). It is guaranteed that there is at least one zero in follow. House numbers (positive numbers) are unique and do not exceed 10^9.


|       Input         |       Output        |
|-----------------|-------------------|
| 5                     |       0 1 2 1 0     |
| 0 1 4 9 0         |                          |
|-----------------|-------------------|
| 6                     |    0 1 2 3 4 5     |
| 0 7 9 4 8 20    |                          |

Task2:

Gosha and Kondraty have found an unusual high-speed typing training machine and want to master it. The simulator is a field of 4x4 keys, in which a configuration of numbers and dots appears each round. Each key is written with either a period or a number from 1 to 9.
At the moment of time t the player must simultaneously press all the keys on which the number t is written. Goshi and Kondraty can press k keys each at the same time. If at the moment of time, all the necessary keys were pressed, then they receive 1 point.
Find the number of points that will help Gosha and Kondraty to earn by pressing the keys together.

The first line contains an integer k, 1 ≤ k ≤ 5.
In the next four lines, the type of simulator is set - 4 characters in each line. Each character is either a dot or from 1 to 9.
Characters of one line are in a row and are not separated by spaces.

|       Input         |       Output        |
|-----------------|-------------------|
|         3             |            2            |
|      1231          |                          |
|       2..2           |                          |
|       2..2           |                          |
|       2..2           |                          |
|-----------------|-------------------|
|           4           |             0           |
|        1111        |                          |
|        1111        |                          |
|        1111        |                          |
|        1111        |                          |
|-----------------|-------------------|

