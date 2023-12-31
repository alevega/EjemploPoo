PGDMP         0            	    {            juego    14.9    14.9     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16404    juego    DATABASE     e   CREATE DATABASE juego WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Argentina.1252';
    DROP DATABASE juego;
                postgres    false            �            1259    16424    fondo    TABLE     _   CREATE TABLE public.fondo (
    fondo_id integer NOT NULL,
    fondo character varying(250)
);
    DROP TABLE public.fondo;
       public         heap    postgres    false            �            1259    16423    fondo_fondo_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fondo_fondo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.fondo_fondo_id_seq;
       public          postgres    false    210            �           0    0    fondo_fondo_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.fondo_fondo_id_seq OWNED BY public.fondo.fondo_id;
          public          postgres    false    209            �            1259    16431    ventana    TABLE     �   CREATE TABLE public.ventana (
    ventana_id integer NOT NULL,
    fondo_id integer,
    nombre character varying(100),
    icono character varying(100),
    altura integer,
    ancho integer
);
    DROP TABLE public.ventana;
       public         heap    postgres    false            �            1259    16430    ventana_ventana_id_seq    SEQUENCE     �   CREATE SEQUENCE public.ventana_ventana_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.ventana_ventana_id_seq;
       public          postgres    false    212            �           0    0    ventana_ventana_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.ventana_ventana_id_seq OWNED BY public.ventana.ventana_id;
          public          postgres    false    211            a           2604    16427    fondo fondo_id    DEFAULT     p   ALTER TABLE ONLY public.fondo ALTER COLUMN fondo_id SET DEFAULT nextval('public.fondo_fondo_id_seq'::regclass);
 =   ALTER TABLE public.fondo ALTER COLUMN fondo_id DROP DEFAULT;
       public          postgres    false    209    210    210            b           2604    16434    ventana ventana_id    DEFAULT     x   ALTER TABLE ONLY public.ventana ALTER COLUMN ventana_id SET DEFAULT nextval('public.ventana_ventana_id_seq'::regclass);
 A   ALTER TABLE public.ventana ALTER COLUMN ventana_id DROP DEFAULT;
       public          postgres    false    211    212    212            �          0    16424    fondo 
   TABLE DATA           0   COPY public.fondo (fondo_id, fondo) FROM stdin;
    public          postgres    false    210   =       �          0    16431    ventana 
   TABLE DATA           U   COPY public.ventana (ventana_id, fondo_id, nombre, icono, altura, ancho) FROM stdin;
    public          postgres    false    212   �       �           0    0    fondo_fondo_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.fondo_fondo_id_seq', 1, true);
          public          postgres    false    209            �           0    0    ventana_ventana_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.ventana_ventana_id_seq', 1, true);
          public          postgres    false    211            d           2606    16429    fondo fondo_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.fondo
    ADD CONSTRAINT fondo_pkey PRIMARY KEY (fondo_id);
 :   ALTER TABLE ONLY public.fondo DROP CONSTRAINT fondo_pkey;
       public            postgres    false    210            f           2606    16436    ventana ventana_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.ventana
    ADD CONSTRAINT ventana_pkey PRIMARY KEY (ventana_id);
 >   ALTER TABLE ONLY public.ventana DROP CONSTRAINT ventana_pkey;
       public            postgres    false    212            �   _   x�Ʊ
�0��>�?:�����m.��1MI��?���k���^��n�f�\�\��e.��-9)E�����ZN{��2D)q�
�B}[r
[B�0 �      �   n   x�ʱ
�0���0����E��]�\B8�s�h�ߺ}�)��4+�|�Go<}�|7��n�cˮ��gG�T�ލg��E��Ɵ�T���"&�5��-k�8{:}xv!�{ $�     