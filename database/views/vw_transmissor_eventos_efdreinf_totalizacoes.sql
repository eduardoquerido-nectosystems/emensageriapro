-- View: public.vw_transmissor_eventos_efdreinf_totalizacoes

DROP VIEW IF EXISTS public.vw_transmissor_eventos_efdreinf_totalizacoes;

CREATE OR REPLACE VIEW public.vw_transmissor_eventos_efdreinf_totalizacoes AS SELECT r5001_evttotal.id,
    'r5001'::text AS evento,
    r5001_evttotal.identidade,
    r5001_evttotal.transmissor_lote_efdreinf_id,
    r5001_evttotal.criado_em,
    r5001_evttotal.criado_por_id,
    r5001_evttotal.modificado_em,
    r5001_evttotal.modificado_por_id,
    r5001_evttotal.desativado_em,
    r5001_evttotal.desativado_por_id,
    r5001_evttotal.ativo,
    4 AS grupo,
    'r5001_evttotal'::text AS tabela,
    'r5001_evttotal_salvar'::text AS tabela_salvar,
    r5001_evttotal.id AS ordem,
    r5001_evttotal.tpinsc,
    r5001_evttotal.nrinsc,
    'r5001_evttotal_recibo'::text AS url_recibo,
    r5001_evttotal.validacao_precedencia,
    r5001_evttotal.validacoes,
    r5001_evttotal.status,
    r5001_evttotal.ocorrencias
   FROM r5001_evttotal
  WHERE r5001_evttotal.ativo = true
 UNION
SELECT r5011_evttotalcontrib.id,
    'r5011'::text AS evento,
    r5011_evttotalcontrib.identidade,
    r5011_evttotalcontrib.transmissor_lote_efdreinf_id,
    r5011_evttotalcontrib.criado_em,
    r5011_evttotalcontrib.criado_por_id,
    r5011_evttotalcontrib.modificado_em,
    r5011_evttotalcontrib.modificado_por_id,
    r5011_evttotalcontrib.desativado_em,
    r5011_evttotalcontrib.desativado_por_id,
    r5011_evttotalcontrib.ativo,
    4 AS grupo,
    'r5011_evttotalcontrib'::text AS tabela,
    'r5011_evttotalcontrib_salvar'::text AS tabela_salvar,
    r5011_evttotalcontrib.id AS ordem,
    r5011_evttotalcontrib.tpinsc,
    r5011_evttotalcontrib.nrinsc,
    'r5011_evttotalcontrib_recibo'::text AS url_recibo,
    r5011_evttotalcontrib.validacao_precedencia,
    r5011_evttotalcontrib.validacoes,
    r5011_evttotalcontrib.status,
    r5011_evttotalcontrib.ocorrencias
   FROM r5011_evttotalcontrib
  WHERE r5011_evttotalcontrib.ativo = true
 UNION
SELECT r9001_evttotal.id,
    'r9001'::text AS evento,
    r9001_evttotal.identidade,
    r9001_evttotal.transmissor_lote_efdreinf_id,
    r9001_evttotal.criado_em,
    r9001_evttotal.criado_por_id,
    r9001_evttotal.modificado_em,
    r9001_evttotal.modificado_por_id,
    r9001_evttotal.desativado_em,
    r9001_evttotal.desativado_por_id,
    r9001_evttotal.ativo,
    4 AS grupo,
    'r9001_evttotal'::text AS tabela,
    'r9001_evttotal_salvar'::text AS tabela_salvar,
    r9001_evttotal.id AS ordem,
    r9001_evttotal.tpinsc,
    r9001_evttotal.nrinsc,
    'r9001_evttotal_recibo'::text AS url_recibo,
    r9001_evttotal.validacao_precedencia,
    r9001_evttotal.validacoes,
    r9001_evttotal.status,
    r9001_evttotal.ocorrencias
   FROM r9001_evttotal
  WHERE r9001_evttotal.ativo = true
 UNION
SELECT r9002_evtret.id,
    'r9002'::text AS evento,
    r9002_evtret.identidade,
    r9002_evtret.transmissor_lote_efdreinf_id,
    r9002_evtret.criado_em,
    r9002_evtret.criado_por_id,
    r9002_evtret.modificado_em,
    r9002_evtret.modificado_por_id,
    r9002_evtret.desativado_em,
    r9002_evtret.desativado_por_id,
    r9002_evtret.ativo,
    4 AS grupo,
    'r9002_evtret'::text AS tabela,
    'r9002_evtret_salvar'::text AS tabela_salvar,
    r9002_evtret.id AS ordem,
    r9002_evtret.tpinsc,
    r9002_evtret.nrinsc,
    'r9002_evtret_recibo'::text AS url_recibo,
    r9002_evtret.validacao_precedencia,
    r9002_evtret.validacoes,
    r9002_evtret.status,
    r9002_evtret.ocorrencias
   FROM r9002_evtret
  WHERE r9002_evtret.ativo = true
 UNION
SELECT r9011_evttotalcontrib.id,
    'r9011'::text AS evento,
    r9011_evttotalcontrib.identidade,
    r9011_evttotalcontrib.transmissor_lote_efdreinf_id,
    r9011_evttotalcontrib.criado_em,
    r9011_evttotalcontrib.criado_por_id,
    r9011_evttotalcontrib.modificado_em,
    r9011_evttotalcontrib.modificado_por_id,
    r9011_evttotalcontrib.desativado_em,
    r9011_evttotalcontrib.desativado_por_id,
    r9011_evttotalcontrib.ativo,
    4 AS grupo,
    'r9011_evttotalcontrib'::text AS tabela,
    'r9011_evttotalcontrib_salvar'::text AS tabela_salvar,
    r9011_evttotalcontrib.id AS ordem,
    r9011_evttotalcontrib.tpinsc,
    r9011_evttotalcontrib.nrinsc,
    'r9011_evttotalcontrib_recibo'::text AS url_recibo,
    r9011_evttotalcontrib.validacao_precedencia,
    r9011_evttotalcontrib.validacoes,
    r9011_evttotalcontrib.status,
    r9011_evttotalcontrib.ocorrencias
   FROM r9011_evttotalcontrib
  WHERE r9011_evttotalcontrib.ativo = true
 UNION
SELECT r9012_evtretcons.id,
    'r9012'::text AS evento,
    r9012_evtretcons.identidade,
    r9012_evtretcons.transmissor_lote_efdreinf_id,
    r9012_evtretcons.criado_em,
    r9012_evtretcons.criado_por_id,
    r9012_evtretcons.modificado_em,
    r9012_evtretcons.modificado_por_id,
    r9012_evtretcons.desativado_em,
    r9012_evtretcons.desativado_por_id,
    r9012_evtretcons.ativo,
    4 AS grupo,
    'r9012_evtretcons'::text AS tabela,
    'r9012_evtretcons_salvar'::text AS tabela_salvar,
    r9012_evtretcons.id AS ordem,
    r9012_evtretcons.tpinsc,
    r9012_evtretcons.nrinsc,
    'r9012_evtretcons_recibo'::text AS url_recibo,
    r9012_evtretcons.validacao_precedencia,
    r9012_evtretcons.validacoes,
    r9012_evtretcons.status,
    r9012_evtretcons.ocorrencias
   FROM r9012_evtretcons
  WHERE r9012_evtretcons.ativo = true;