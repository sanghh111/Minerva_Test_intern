<center><h3>BACKEND ENGINEER INTERNSHIP </h3></center>

<ol type = "I">

<h5><li>SQL</li></h5>
<ol>
<li> Write a query that selects student_id and number of absent dates for each user who has more than 3 absent dates. Check-in dates are distinct<br></li>

Querry is:
<code>select student_id , count() as "absent dates"
From attendance as a1
GROUP BY(student_id)
Having count(absent_flag) > 3
</code>
 



You can work shell by:
<code>from Section1 import connect_db

for items in connect_db.check_absent_date_gt_3():
&#160;&#160;&#160;&#160;print('student id: {}, absent date: {}'.format(items[0],items[1]))
</code>

<li>How many types of pagination in SQL?</li>
It have two types of pagination in SQL
<ul>
<li>OFFSET</li>
<li>FETCH </li>
</ul>

</ol>
<h5><li>Section 2: Coding Challenge</li></h5>
<ol>
<li>Two Poiters: A pair (i, j) is called good if nums[i] == nums[j] and i < j. Given an array of integer numbers. List all pairs (i, j)</li>

<ul>
<li>Example 1:<br>
- Input: nums = [1,2,3,1,1,3]<br>
- Output: [(0,3), (0,4), (3,4), (2,5)]<br>
- Explanation: There are 4 good pairs:<br>
nums[0] = nums[3] = 1<br>
nums[0] = nums[4] = 1<br>
nums[3] = nums[4] = 1<br>
nums[2] = nums[5] = 3<br>
</li>
<br>
<li>Example 2:<br>
- Input: nums = [1,1,1,1]<br>
- Output: 6<br>
- Explanation: There are 6 good pairs:<br>
nums[0] = nums[1] = 1<br>
nums[0] = nums[2] = 1<br>
nums[0] = nums[3] = 1<br>
nums[1] = nums[2] = 1<br>
nums[1] = nums[3] = 1<br>
nums[2] = nums[3] = 1<br>
</li>
<br>
<li>Example 3:<br>
- Input: nums = [1,2,3]<br>
- Output: [ ]<br>
- Explanation: There are 0 good pairs.<br>
</li><br>

</ul>

My idea: The first create a empty list purpose is the output then i create frist pointer loop from in  frist  list to near end  list. Each i create second pointer loop from first pointer plus 1 to end list. if i see value position first pointer equal second pointer then i append output list is tupple fotmat(position first pointer and second pointer)

Work on shell:
<code>from Section2 import solusion1</code>

funcion:<code>solution_1(string)</code> return list all pairs (i, j)

<li>Write code to solve the below problem:</li> A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; I.e: b occurs no more times than a; c occurs no more times than b; etc. Note that letter a has no previous letter. Given a string, check whether it is beautiful.

Example 1:

<ul><li>Input: input_string = “bbbaacdafe”</li>
<li>Output: is_beautiful_string(input_string) = True</li>
<li>Explanation: This string contains 3 a, 3 b, 1 c, 1 d, 1 e, and 1 f (and 0 of every other letter), so since there aren't any letters that appear more frequently than the previous letter, this string qualifies as beautiful.</li>
</ul>
<br>
Example 2:
<ul>
<li>Input: input_string = “aabbb”
<li>Output: is_beautiful_string(input_string) = False
<li>Explanation: Since there are more bs than as, this string is not beautiful.
</ul><br>
Example 3:
<ul>
<li>Input: input_string = “bbbbcbaacdafe”
<li>Output: is_beautiful_string(input_string) = False
<li>Explanation: Although there are more b than c, this string is not beautiful because there are no a, so therefore there are more b than a.
</ul><br>

<b>Note:</b>
<ul>
<li>A string of lowercase English letters.
<li>Guaranteed constraints:
    <ul>
    <li>3 ≤ inputString.length ≤ 50.
    <li>[output] boolean: Return true if the string is beautiful, false otherwise
    </ul>
</ul>
</ol>

My idea: Find a max character then i find position in the alphabet then i plus one. Create a list with length equal position i find it and value each item in list equal zero with purpose is source appear in the input. Final i check couple from posion first list to end list if the fist value less i return false and if i find 1 value equal zero i return False

Work on shell:
<code>from Section2 import solusion2</code>

funcion:<code>is_beautiful_string(string)</code> Return true if the string is beautiful, false otherwise

</ol>

