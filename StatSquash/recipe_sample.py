new_users_month = {
    'title': 'Registered Users (monthly)',
    'type': 'line',
    'headers': ['Date', 'Users'],
    'data': ['change_registered_users']
}

posts_comments_month = {
    'title': 'Posts vs. Comments (monthly)',
    'type': 'line',
    'headers': ['Date', 'Posts', 'Comments'],
    'data': ['change_posts', 'change_comments']
}

cookbook = [
    new_users_month,
    posts_comments_month
]