use publications;
# Challenge 1
select titles.title, titles.title_id, titleauthor.au_id, authors.au_fname as First_name, authors.au_lname as Last_name, pub_name
from titles
left join publishers
on titles.pub_id = publishers.pub_id
left join titleauthor
on titles.title_id = titleauthor.title_id
left join authors
on authors.au_id = titleauthor.au_id 
;

#Challenge 	2

Create temporary table solution_chllge1
select titles.title, titles.title_id, titleauthor.au_id, authors.au_fname as First_name, authors.au_lname as Last_name, pub_name
from titles
left join publishers
on titles.pub_id = publishers.pub_id
left join titleauthor
on titles.title_id = titleauthor.title_id
left join authors
on authors.au_id = titleauthor.au_id 
;

Select au_id as author_ID, First_name, Last_name, pub_name as publisher, count(distinct(title_id)) as title_count
from solution_chllge1
group by author_ID, First_name, Last_name, publisher
order by title_count desc
;

# Challenge 3

select titleauthor.au_id as Author_ID, authors.au_fname as First_name, authors.au_lname as Last_name, sum(sales.qty) as unidades_compradas
from titles
left join sales
on sales.title_id=titles.title_id
left join titleauthor
on titles.title_id=titleauthor.title_id
left join authors
on authors.au_id=titleauthor.au_id
group by Author_ID
order by unidades_compradas desc
limit 3
;

# Challenge 4

select titleauthor.au_id as Author_ID, authors.au_fname as First_name, authors.au_lname as Last_name, sum(sales.qty) as unidades_compradas
from titles
left join sales
on sales.title_id=titles.title_id
left join titleauthor
on titles.title_id=titleauthor.title_id
left join authors
on authors.au_id=titleauthor.au_id
group by Author_ID
order by unidades_compradas desc
;