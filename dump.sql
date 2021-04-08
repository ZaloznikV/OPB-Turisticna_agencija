--
-- PostgreSQL database dump
--

-- Dumped from database version 9.4.8
-- Dumped by pg_dump version 10.16 (Ubuntu 10.16-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: atrakcije; Type: TABLE; Schema: public; Owner: vitoz
--

CREATE TABLE public.atrakcije (
    atrakcija text NOT NULL
);


ALTER TABLE public.atrakcije OWNER TO vitoz;

--
-- Name: atrakcijepodrzavah; Type: TABLE; Schema: public; Owner: vitoz
--

CREATE TABLE public.atrakcijepodrzavah (
    "država" text,
    atrakcija text
);


ALTER TABLE public.atrakcijepodrzavah OWNER TO vitoz;

--
-- Name: države; Type: TABLE; Schema: public; Owner: vitoz
--

CREATE TABLE public."države" (
    "država" text NOT NULL,
    opis text
);


ALTER TABLE public."države" OWNER TO vitoz;

--
-- Name: izlet; Type: TABLE; Schema: public; Owner: vitoz
--

CREATE TABLE public.izlet (
    id integer NOT NULL,
    oseba integer,
    "državazačetek" text,
    "državakonec" text,
    prevoz text,
    datum date NOT NULL,
    ocena integer NOT NULL
);


ALTER TABLE public.izlet OWNER TO vitoz;

--
-- Name: možnitransporti; Type: TABLE; Schema: public; Owner: vitoz
--

CREATE TABLE public."možnitransporti" (
    "državazačetek" text,
    "državakonec" text,
    prevoz text,
    trajanje integer NOT NULL,
    cena integer NOT NULL
);


ALTER TABLE public."možnitransporti" OWNER TO vitoz;

--
-- Name: osebe; Type: TABLE; Schema: public; Owner: vitoz
--

CREATE TABLE public.osebe (
    "emšo" integer NOT NULL,
    ime text NOT NULL,
    priimek text NOT NULL,
    "državljanstvo" text,
    email text NOT NULL,
    geslo text NOT NULL
);


ALTER TABLE public.osebe OWNER TO vitoz;

--
-- Name: prevoz; Type: TABLE; Schema: public; Owner: vitoz
--

CREATE TABLE public.prevoz (
    prevoz text NOT NULL
);


ALTER TABLE public.prevoz OWNER TO vitoz;

--
-- Data for Name: atrakcije; Type: TABLE DATA; Schema: public; Owner: vitoz
--



--
-- Data for Name: atrakcijepodrzavah; Type: TABLE DATA; Schema: public; Owner: vitoz
--



--
-- Data for Name: države; Type: TABLE DATA; Schema: public; Owner: vitoz
--



--
-- Data for Name: izlet; Type: TABLE DATA; Schema: public; Owner: vitoz
--



--
-- Data for Name: možnitransporti; Type: TABLE DATA; Schema: public; Owner: vitoz
--



--
-- Data for Name: osebe; Type: TABLE DATA; Schema: public; Owner: vitoz
--



--
-- Data for Name: prevoz; Type: TABLE DATA; Schema: public; Owner: vitoz
--



--
-- Name: atrakcije atrakcije_atrakcija_key; Type: CONSTRAINT; Schema: public; Owner: vitoz
--

ALTER TABLE ONLY public.atrakcije
    ADD CONSTRAINT atrakcije_atrakcija_key UNIQUE (atrakcija);


--
-- Name: države države_država_key; Type: CONSTRAINT; Schema: public; Owner: vitoz
--

ALTER TABLE ONLY public."države"
    ADD CONSTRAINT "države_država_key" UNIQUE ("država");


--
-- Name: izlet izlet_pkey; Type: CONSTRAINT; Schema: public; Owner: vitoz
--

ALTER TABLE ONLY public.izlet
    ADD CONSTRAINT izlet_pkey PRIMARY KEY (id);


--
-- Name: osebe osebe_pkey; Type: CONSTRAINT; Schema: public; Owner: vitoz
--

ALTER TABLE ONLY public.osebe
    ADD CONSTRAINT osebe_pkey PRIMARY KEY ("emšo");


--
-- Name: prevoz prevoz_prevoz_key; Type: CONSTRAINT; Schema: public; Owner: vitoz
--

ALTER TABLE ONLY public.prevoz
    ADD CONSTRAINT prevoz_prevoz_key UNIQUE (prevoz);


--
-- Name: atrakcijepodrzavah atrakcijepodrzavah_atrakcija_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vitoz
--

ALTER TABLE ONLY public.atrakcijepodrzavah
    ADD CONSTRAINT atrakcijepodrzavah_atrakcija_fkey FOREIGN KEY (atrakcija) REFERENCES public.atrakcije(atrakcija);


--
-- Name: atrakcijepodrzavah atrakcijepodrzavah_država_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vitoz
--

ALTER TABLE ONLY public.atrakcijepodrzavah
    ADD CONSTRAINT "atrakcijepodrzavah_država_fkey" FOREIGN KEY ("država") REFERENCES public."države"("država");


--
-- Name: izlet izlet_državakonec_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vitoz
--

ALTER TABLE ONLY public.izlet
    ADD CONSTRAINT "izlet_državakonec_fkey" FOREIGN KEY ("državakonec") REFERENCES public."države"("država");


--
-- Name: izlet izlet_državazačetek_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vitoz
--

ALTER TABLE ONLY public.izlet
    ADD CONSTRAINT "izlet_državazačetek_fkey" FOREIGN KEY ("državazačetek") REFERENCES public."države"("država");


--
-- Name: izlet izlet_oseba_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vitoz
--

ALTER TABLE ONLY public.izlet
    ADD CONSTRAINT izlet_oseba_fkey FOREIGN KEY (oseba) REFERENCES public.osebe("emšo");


--
-- Name: izlet izlet_prevoz_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vitoz
--

ALTER TABLE ONLY public.izlet
    ADD CONSTRAINT izlet_prevoz_fkey FOREIGN KEY (prevoz) REFERENCES public.prevoz(prevoz);


--
-- Name: možnitransporti možnitransporti_državakonec_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vitoz
--

ALTER TABLE ONLY public."možnitransporti"
    ADD CONSTRAINT "možnitransporti_državakonec_fkey" FOREIGN KEY ("državakonec") REFERENCES public."države"("država");


--
-- Name: možnitransporti možnitransporti_državazačetek_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vitoz
--

ALTER TABLE ONLY public."možnitransporti"
    ADD CONSTRAINT "možnitransporti_državazačetek_fkey" FOREIGN KEY ("državazačetek") REFERENCES public."države"("država");


--
-- Name: možnitransporti možnitransporti_prevoz_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vitoz
--

ALTER TABLE ONLY public."možnitransporti"
    ADD CONSTRAINT "možnitransporti_prevoz_fkey" FOREIGN KEY (prevoz) REFERENCES public.prevoz(prevoz);


--
-- Name: osebe osebe_državljanstvo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vitoz
--

ALTER TABLE ONLY public.osebe
    ADD CONSTRAINT "osebe_državljanstvo_fkey" FOREIGN KEY ("državljanstvo") REFERENCES public."države"("država");


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: vitoz
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM vitoz;
GRANT ALL ON SCHEMA public TO vitoz;
GRANT USAGE ON SCHEMA public TO PUBLIC;
GRANT ALL ON SCHEMA public TO vitoz_mktg;
GRANT ALL ON SCHEMA public TO andrazpu;
GRANT ALL ON SCHEMA public TO urbanc;


--
-- PostgreSQL database dump complete
--

