PGDMP     1    1                {            juego    15.4    15.4     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    24586    juego    DATABASE     |   CREATE DATABASE juego WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Argentina.1252';
    DROP DATABASE juego;
                postgres    false            �            1259    24588    configuracion    TABLE     �   CREATE TABLE public.configuracion (
    id integer NOT NULL,
    nombre_ventana character varying,
    altura integer,
    ancho integer,
    icono character varying,
    fondo character varying
);
 !   DROP TABLE public.configuracion;
       public         heap    postgres    false            �            1259    24587    congfiguracion_id_seq    SEQUENCE     �   CREATE SEQUENCE public.congfiguracion_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.congfiguracion_id_seq;
       public          postgres    false    215            �           0    0    congfiguracion_id_seq    SEQUENCE OWNED BY     N   ALTER SEQUENCE public.congfiguracion_id_seq OWNED BY public.configuracion.id;
          public          postgres    false    214            e           2604    24591    configuracion id    DEFAULT     u   ALTER TABLE ONLY public.configuracion ALTER COLUMN id SET DEFAULT nextval('public.congfiguracion_id_seq'::regclass);
 ?   ALTER TABLE public.configuracion ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215            �          0    24588    configuracion 
   TABLE DATA           X   COPY public.configuracion (id, nombre_ventana, altura, ancho, icono, fondo) FROM stdin;
    public          postgres    false    215   T       �           0    0    congfiguracion_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.congfiguracion_id_seq', 1, false);
          public          postgres    false    214            g           2606    24595 !   configuracion congfiguracion_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.configuracion
    ADD CONSTRAINT congfiguracion_pkey PRIMARY KEY (id);
 K   ALTER TABLE ONLY public.configuracion DROP CONSTRAINT congfiguracion_pkey;
       public            postgres    false    215            �   t   x�3��*MM�Wp�J�-���44�0�472�t��-N-*��)M�����Ku)�,K�w-N.�,�/�����ׇ�1�sS�3s�S�R��3������
�)6)7� �H� /�+F��� I<�     