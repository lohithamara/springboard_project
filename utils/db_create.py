import sqlite3
db_path = "sentiment_analysis.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

#Sentence_Database table
cursor.execute('''
	CREATE TABLE IF NOT EXISTS Sentence_Database (
		sentence TEXT,
		score INTEGER,
		sentiment TEXT CHECK(sentiment IN ('positive', 'negative'))
	)
''')

#Word_list_database table
cursor.execute('''
	CREATE TABLE IF NOT EXISTS word_list_database (
		word TEXT,
		sentiment TEXT CHECK(sentiment IN ('positive', 'negative')),
		is_available_in_dict BOOLEAN

	)
''')

#Analysis_database table
cursor.execute('''
	CREATE TABLE IF NOT EXISTS Analysis_database (
		total_sentences INTEGER,
		total_paras INTEGER,
		total_score INTEGER,
		total_words INTEGER,
		total_negative_words INTEGER,
		total_positive_words INTEGER,
		total_dict_hits INTEGER,
		total_dict_miss INTEGER,
		total_positive_sentences INTEGER,
		total_negative_sentences INTEGER
	)
''')

conn.commit()
conn.close()