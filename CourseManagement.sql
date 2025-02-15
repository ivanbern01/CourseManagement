PGDMP  $                     }            CourseManagement    17.1    17.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    16765    CourseManagement    DATABASE     �   CREATE DATABASE "CourseManagement" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
 "   DROP DATABASE "CourseManagement";
                     postgres    false            �            1259    16770    students    TABLE     '  CREATE TABLE public.students (
    id integer NOT NULL,
    first_name character varying(50),
    middle_name character varying(50),
    last_name character varying(50),
    age integer,
    course character varying(100),
    email character varying(100),
    password character varying(255)
);
    DROP TABLE public.students;
       public         heap r       postgres    false            �            1259    16769    students_id_seq    SEQUENCE     �   CREATE SEQUENCE public.students_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.students_id_seq;
       public               postgres    false    218            �           0    0    students_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;
          public               postgres    false    217            W           2604    16773    students id    DEFAULT     j   ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);
 :   ALTER TABLE public.students ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    218    217    218            �          0    16770    students 
   TABLE DATA           h   COPY public.students (id, first_name, middle_name, last_name, age, course, email, password) FROM stdin;
    public               postgres    false    218   �       �           0    0    students_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.students_id_seq', 11, true);
          public               postgres    false    217            Y           2606    16779    students students_email_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_email_key UNIQUE (email);
 E   ALTER TABLE ONLY public.students DROP CONSTRAINT students_email_key;
       public                 postgres    false    218            [           2606    16777    students students_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.students DROP CONSTRAINT students_pkey;
       public                 postgres    false    218            �   �  x�m�]��:��˯�s���!��GTD���@��|��~;�ٓ9q��&�J�z���e�`V�d��� ��ʮ%�/'�$	H�Gب o䊳�Bذ�@���D���i�����I ��9���#����@�"�i,��F���,|W,�Eh|�:���S��tjnN.���p�E�%����oZ�,�:���R�^q�)ʕ�i�F^)��!�w�.d�+�җ�T������&i�1<H2�5�\
�3�I8�s��3�/TEs�:���Tơaq�ۭ�X�ɓ�T5{��x>�SS�QF K��旒G5�`���ցu]�u�}�}��ݷ��9����AG_=�u���U�1�'ڲ�4\_�6\�����f�?"3"�C�G�@�s�>���^�4���M�^Z�q屶$Ұ����U]G� kw\�"@j��L��~# �Ao���J��|L�<\s�� �
?.��J��v�_����ڱ�� >|;� ��_��U`���db1gpv)�N9cc�&6�ڿΨSXa�12����$����pG�H��%�����C7@�9�U;WT7�D�bj�2���5�`��@)' �A����8��g'Y��+�[%V:X;s�D���z�Ԯu<,,�$���1W����꺭[@ꖴ��!����W�ķ�c��}����۳~�-xnD3�؝J����R�m�Xf�e��g�]+     