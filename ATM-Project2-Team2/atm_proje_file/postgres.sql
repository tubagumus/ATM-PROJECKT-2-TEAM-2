PGDMP     7    4                {            postgres    14.7    14.7 !    "           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            #           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            $           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            %           1262    13754    postgres    DATABASE     e   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Turkish_Turkey.1254';
    DROP DATABASE postgres;
                postgres    false            &           0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    3365                        3079    16384 	   adminpack 	   EXTENSION     A   CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;
    DROP EXTENSION adminpack;
                   false            '           0    0    EXTENSION adminpack    COMMENT     M   COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';
                        false    2            �            1259    24613    accountList    TABLE     +  CREATE TABLE public."accountList" (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    surname character varying(15) NOT NULL,
    balance integer NOT NULL,
    "e-mail" character varying(25) NOT NULL,
    "tax-number" integer NOT NULL,
    password character varying NOT NULL
);
 !   DROP TABLE public."accountList";
       public         heap    postgres    false            �            1259    24600    againtablecreate    TABLE     �   CREATE TABLE public.againtablecreate (
    id integer NOT NULL,
    ad character varying(20) NOT NULL,
    marka character varying(20),
    stok integer,
    katagori character varying(20)
);
 $   DROP TABLE public.againtablecreate;
       public         heap    postgres    false            �            1259    24605    againtablecreate2    TABLE     �   CREATE TABLE public.againtablecreate2 (
    id integer NOT NULL,
    ad character varying(20) NOT NULL,
    marka character varying(20),
    stok integer,
    katagori character varying(20)
);
 %   DROP TABLE public.againtablecreate2;
       public         heap    postgres    false            �            1259    24583    csv.csv    TABLE     i   CREATE TABLE public."csv.csv" (
    name character varying[],
    vise integer[],
    final integer[]
);
    DROP TABLE public."csv.csv";
       public         heap    postgres    false            �            1259    24576    csvfor    TABLE     s   CREATE TABLE public.csvfor (
    name character varying(50)[] NOT NULL,
    vise integer[],
    final integer[]
);
    DROP TABLE public.csvfor;
       public         heap    postgres    false            �            1259    24588    forimportcsv    TABLE     �   CREATE TABLE public.forimportcsv (
    name character varying NOT NULL,
    "3" character varying,
    "5" character varying,
    "6" character varying,
    "7" character varying,
    "2" character varying,
    "4" character varying
);
     DROP TABLE public.forimportcsv;
       public         heap    postgres    false            �            1259    16402    payment    TABLE     �   CREATE TABLE public.payment (
    payment_id integer NOT NULL,
    customer_id integer NOT NULL,
    "stuff id" integer NOT NULL,
    rental_id integer NOT NULL,
    amount integer NOT NULL,
    payment_date integer NOT NULL
);
    DROP TABLE public.payment;
       public         heap    postgres    false            �            1259    24620    tryTable    TABLE     �   CREATE TABLE public."tryTable" (
    "1" character varying NOT NULL,
    "22" character varying,
    "3" character varying,
    "4" character varying,
    "5" character varying,
    "6" character varying,
    "7" character varying
);
    DROP TABLE public."tryTable";
       public         heap    postgres    false            �            1259    24595    urunn    TABLE     �   CREATE TABLE public.urunn (
    id integer NOT NULL,
    ad character varying(20) NOT NULL,
    marka character varying(20),
    stok integer,
    katagori character varying(20)
);
    DROP TABLE public.urunn;
       public         heap    postgres    false                      0    24613    accountList 
   TABLE DATA           e   COPY public."accountList" (id, name, surname, balance, "e-mail", "tax-number", password) FROM stdin;
    public          postgres    false    217   $                 0    24600    againtablecreate 
   TABLE DATA           I   COPY public.againtablecreate (id, ad, marka, stok, katagori) FROM stdin;
    public          postgres    false    215   l$                 0    24605    againtablecreate2 
   TABLE DATA           J   COPY public.againtablecreate2 (id, ad, marka, stok, katagori) FROM stdin;
    public          postgres    false    216   �$                 0    24583    csv.csv 
   TABLE DATA           6   COPY public."csv.csv" (name, vise, final) FROM stdin;
    public          postgres    false    212   �$                 0    24576    csvfor 
   TABLE DATA           3   COPY public.csvfor (name, vise, final) FROM stdin;
    public          postgres    false    211   �$                 0    24588    forimportcsv 
   TABLE DATA           J   COPY public.forimportcsv (name, "3", "5", "6", "7", "2", "4") FROM stdin;
    public          postgres    false    213   �$                 0    16402    payment 
   TABLE DATA           g   COPY public.payment (payment_id, customer_id, "stuff id", rental_id, amount, payment_date) FROM stdin;
    public          postgres    false    210   q'                 0    24620    tryTable 
   TABLE DATA           H   COPY public."tryTable" ("1", "22", "3", "4", "5", "6", "7") FROM stdin;
    public          postgres    false    218   �'                 0    24595    urunn 
   TABLE DATA           >   COPY public.urunn (id, ad, marka, stok, katagori) FROM stdin;
    public          postgres    false    214   �'       �           2606    24619    accountList accountList_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public."accountList"
    ADD CONSTRAINT "accountList_pkey" PRIMARY KEY (id);
 J   ALTER TABLE ONLY public."accountList" DROP CONSTRAINT "accountList_pkey";
       public            postgres    false    217            �           2606    24609 (   againtablecreate2 againtablecreate2_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.againtablecreate2
    ADD CONSTRAINT againtablecreate2_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.againtablecreate2 DROP CONSTRAINT againtablecreate2_pkey;
       public            postgres    false    216            �           2606    24604 &   againtablecreate againtablecreate_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.againtablecreate
    ADD CONSTRAINT againtablecreate_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.againtablecreate DROP CONSTRAINT againtablecreate_pkey;
       public            postgres    false    215                       2606    24582    csvfor csvfor_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.csvfor
    ADD CONSTRAINT csvfor_pkey PRIMARY KEY (name);
 <   ALTER TABLE ONLY public.csvfor DROP CONSTRAINT csvfor_pkey;
       public            postgres    false    211            �           2606    24594    forimportcsv forimportcsv_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.forimportcsv
    ADD CONSTRAINT forimportcsv_pkey PRIMARY KEY (name);
 H   ALTER TABLE ONLY public.forimportcsv DROP CONSTRAINT forimportcsv_pkey;
       public            postgres    false    213            }           2606    16406    payment payment_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_pkey PRIMARY KEY (payment_id);
 >   ALTER TABLE ONLY public.payment DROP CONSTRAINT payment_pkey;
       public            postgres    false    210            �           2606    24626    tryTable tryTable_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public."tryTable"
    ADD CONSTRAINT "tryTable_pkey" PRIMARY KEY ("1");
 D   ALTER TABLE ONLY public."tryTable" DROP CONSTRAINT "tryTable_pkey";
       public            postgres    false    218            �           2606    24599    urunn urunn_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.urunn
    ADD CONSTRAINT urunn_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.urunn DROP CONSTRAINT urunn_pkey;
       public            postgres    false    214               D   x�34 CN�����% �X���ihbbbn©��[�]鐞���������iiabfj�ihd����� ��            x������ � �            x������ � �            x������ � �            x������ � �         �  x�u��n�0��΃�X��,i�tN�I�C/��Zje)�ew~�)�m�l�R"���Ejk�-^���͞�0�rv����o���V;�?[�8�B���փk�WB����'��Q'Nb�NҶd~0]H�b�[uk>��.����Αkǵ�F�Q�y:���D<C�v�2�<KlM�;"y���4r2�E^?AG�<�h����S.�[,z')� �|2���v�)G���Ǥ��{驦��#���2=ѾQ�5���,���5Ć$}�mH��8L�{UL�.]�䥾�F�#V[J�t
�����
km��{IsgV��ȳ���˾KHƱ�}I_#RGi{��:j0�����Ǐ��$���q!�A�6x&7,�D-!_*�u�:����̈́��<Φh]��a���k�R����M>�W���q��������MިŎp&9M����;����N�����rO��1��*��GT_���q���Q�X�E䎳ȯ�ہ�/b�e��ymC�้1��lB�O �Oho��[7}����Oe��_��r�>3��E8�y,�T�����#ɈZ��ٛ*��=T"���z\(��]���P������m6�]��Une�ׯ��{ӊu7Uh�������f6��n��            x������ � �         '   x�S�5R�T2V�TOT�T/��DY"23չb���� ���            x������ � �     