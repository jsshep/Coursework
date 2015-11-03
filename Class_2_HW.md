##1. In Chipotle.tsv, each row represents a single item ordered within a given order (steak burrito, chips and salsa, etc.). ##Each column provides data about that item ordered (quantity, order id, item name, choice, and item price)
head chipotle.tsv
tail chipotle.tsv

##2. There appear to be 1834 orders.
tail chipotle.tsv

##3. 4623
wc chipotle.tsv

##4. Chicken burritos (553) are more popular than steak burritos (368)
grep -c 'Chicken Burrito' chipotle.tsv
grep -c 'Steak Burrito' chipotle.tsv

##5. Chicken burritos more frequently are served with black beans (282) than pinto (105)
grep 'Chicken Burrito' chipotle.tsv > chicken.tsv
grep -c 'Black Beans' chicken.tsv
grep -c 'Pinto Beans' chicken.tsv

##6 
ls *
02_git_github.pdf	README.md		new_file.md		syllabus.md

code:
00_python_beginner_workshop.py			02_command_line_with_intermediate_advanced.md
00_python_intermediate_workshop.py		03_file_reading.py
02_command_line_basics.md			04_pandas.py

data:
airlines.csv		drinks.csv		sms.tsv			u.user_original		yelp.json
bank-additional.csv	example.html		titanic.csv		ufo.csv
bikeshare.csv		hitters.csv		u.data			vehicles_test.csv
chicken.tsv		imdb_1000.csv		u.item			vehicles_train.csv
chipotle.tsv		imdb_ids.txt		u.user			yelp.csv

homework:
02_command_line_chipotle.md	10_yelp_votes.md		14_spam_filtering.md
03_python_homework_chipotle.py	13_cross_validation.md		14_yelp_review_text.md
09_bias_variance.md		13_roc_auc.md

notebooks:
03_python_homework_chipotle_explained.ipynb	12_logistic_regression.ipynb
05_pandas_merge.ipynb				12_titanic_confusion.ipynb
05_pandas_visualization.ipynb			13_advanced_model_evaluation.ipynb
06_human_learning_iris.ipynb			13_bank_exercise.ipynb
08_bias_variance.ipynb				13_cross_validation.ipynb
08_knn_sklearn.ipynb				14_bayes_theorem_iris.ipynb
08_nba_knn.ipynb				14_naive_bayes_spam.ipynb
08_pandas_review.ipynb				14_text_data_sklearn.ipynb
09_model_evaluation.ipynb			14_types_of_naive_bayes.ipynb
10_linear_regression.ipynb			14_yelp_review_text_homework.ipynb
10_yelp_votes_homework.ipynb			15_natural_language_processing.ipynb
12_e_log_examples.ipynb				images

other:
02_exercise_output.png		model_evaluation_comparison.md	setup_checklist.md
02_file_tree.png		python_packages.md		test_subdirectory
git-cheat-sheet.pdf		python_reference
model_comparison.md		scikit-learn_videos

parked:
01_Lesson	misc_resources

project:
README.md		peer_review.md		project_examples	public_data.md

slides:
01_course_overview.pdf		01_types_of_data.pdf		02_git_github2.pd.pdf
01_data_science_intro.pdf	02_git_github.pdf

##7. 
