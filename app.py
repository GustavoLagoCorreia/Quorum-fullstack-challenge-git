import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)


def load_data():
    """Load data from CSV files."""
    bills = pd.read_csv('data/bills.csv')
    legislators = pd.read_csv('data/legislators.csv')
    votes = pd.read_csv('data/votes.csv')
    vote_results = pd.read_csv('data/vote_results.csv')
    return bills, legislators, votes, vote_results


def preprocess_vote_results(vote_results, legislators):
    """Map vote types and merge with legislator names."""
    vote_results['vote_type'] = vote_results['vote_type'].replace({1: 'support', 2: 'oppose'})
    vote_results = vote_results.merge(
        legislators[['id', 'name']], 
        left_on='legislator_id', 
        right_on='id', 
        suffixes=('', '_legislator')
    )
    vote_results.rename(columns={'name': 'legislator_name'}, inplace=True)
    return vote_results


def filter_votes_by_bill(vote_results, selected_bill_id):
    """Filter vote results by the selected bill ID."""
    if selected_bill_id:
        return vote_results[vote_results['vote_id'] == int(selected_bill_id)]
    return vote_results


def summarize_legislators(vote_results):
    """Create a summary of legislators with their supported and opposed bills."""
    summary = (
        vote_results.groupby(['legislator_id', 'legislator_name'])['vote_type']
        .value_counts()
        .unstack(fill_value=0)
        .reset_index()
    )
    summary.columns.name = None
    summary.rename(columns={'legislator_id': 'ID', 'support': 'Supported_bills', 'oppose': 'Opposed_bills'}, inplace=True)
    return summary


def summarize_bills(vote_results, votes, bills, legislators):
    """Create a summary of bills with their supporters and opposers."""
    vote_results = vote_results.merge(votes[['id', 'bill_id']], left_on='vote_id', right_on='id', how='left')
    
    summary = (
        vote_results.groupby('bill_id')['vote_type']
        .value_counts()
        .unstack(fill_value=0)
        .reset_index()
    )
    
    summary = summary.merge(bills[['id', 'title', 'Primary_Sponsor']], left_on='bill_id', right_on='id', how='left')
    
    summary = summary.merge(
        legislators[['id', 'name']], 
        left_on='Primary_Sponsor', 
        right_on='id', 
        how='left'
    )
    
    summary.rename(columns={
        'id_x': 'ID', 
        'support': 'Supporters', 
        'oppose': 'Opposers', 
        'name': 'Primary_Sponsor_name'
    }, inplace=True)

    summary.drop(columns=[col for col in summary.columns if 'id' in col], inplace=True)

    return summary


def summarize_votes(vote_results, bills, votes):
    """Create a summary of votes with associated bill titles."""
    summary = vote_results.merge(votes, left_on='vote_id', right_on='id', suffixes=('', '_vote'))
    summary = summary.merge(bills[['id', 'title']], left_on='bill_id', right_on='id', suffixes=('', '_bill'))
    summary.rename(columns={'title': 'bill_title'}, inplace=True)
    return summary


def clean_nan(clean_df):
    ''' renamed NAN field to not found when can't found '''
    clean_df = clean_df.fillna('not found')
    return clean_df


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        bills, legislators, votes, vote_results = load_data()
        vote_results = preprocess_vote_results(vote_results, legislators)

        selected_bill_id = request.form.get('bill_id')
        vote_results = filter_votes_by_bill(vote_results, selected_bill_id)

        legislator_summary = summarize_legislators(vote_results)
        bill_summary = summarize_bills(vote_results, votes, bills, legislators)
        vote_summary = summarize_votes(vote_results, bills, votes)
        
        legislator_summary = clean_nan(legislator_summary)
        bill_summary = clean_nan(bill_summary)
        vote_summary = clean_nan(vote_summary)

        return render_template('index.html', legislators=legislator_summary, bills=bill_summary, votes=vote_summary)
    
    except Exception as e:
        print(f"Exception error: {e}")


if __name__ == '__main__':
    app.run(debug=True)