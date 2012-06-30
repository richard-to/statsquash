create table monthly_data(
    id bigint unsigned not null primary key auto_increment,
    label varchar(40) not null,
    value int not null,
    created_at timestamp not null,
    unique(label, created_at)
) engine=innodb;
