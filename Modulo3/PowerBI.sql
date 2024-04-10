create table clientes (
    id serial primary key,
    nome varchar (255) not null,
    sobrenome varchar (255) not null,
    email varchar (255) not null 
)

select * from clientes;

insert into clientes values(1, 'Vinicius', 'Granço', 'vini@gmail.com');
insert into clientes values(2, 'João', 'Silva', 'joao@gmail.com');
insert into clientes values(3, 'Pedro', 'Mateus', 'pedro@gmail.com');
insert into clientes values(4, 'Bruno', 'Mendes', 'bruno@gmail.com');
insert into clientes values(5, 'Diogo', 'Thomaz', 'diogo@gmail.com');
insert into clientes values(6, 'Afonso', 'Cristino', 'afonso@gmail.com');

create table pedidos (
    id serial primary  key,
    id_clientes int,
    data_pedido date not null,
    total numeric (6, 2) not null,
    status varchar(255) check (status in ('Em Andamento', 'Finalizado', 'Cancelado')),
    foreign key (id_clientes) references clientes(id)
)

insert into pedidos (id_clientes, data_pedido, total) values (1, '2024-04-01', 100);
insert into pedidos (id_clientes, data_pedido, total) values (2, '2024-05-01', 200);
insert into pedidos (id_clientes, data_pedido, total) values (3, '2024-06-01', 300);
insert into pedidos (id_clientes, data_pedido, total) values (4, '2024-07-01', 400);
insert into pedidos (id_clientes, data_pedido, total) values (5, '2024-08-01', 500);
insert into pedidos (id_clientes, data_pedido, total) values (6, '2024-09-01', 600);

alter table pedidos 
  alter column status 
  set default 'Em Andamento';