CREATE TABLE prim_todo(
	--Datos de niño
	idPersona INT PRIMARY KEY,
	participante TEXT,
	escuela TEXT,
	grado_escolar TEXT,
	edad INT,
	sexo TEXT,

	--Prueba 1
	el_es_una_pelota_de_fuego TEXT,
	a1 INT,
	es_una_pelota_de_plata TEXT,
	a2 INT,
	mi_es_una_pelota_de_pelos TEXT,
	a3 INT,
	por_que_pelota_que_canta_si TEXT,
	a4s INT,
	por_que_pelota_que_canta_no TEXT,
	a4n INT,
	explica_lo_que_quiere_decir_mi_hermanito_es_una_pelota_de_grito TEXT,
	a5 INT,
	que_otra_cosa_podria_ser_una_pelota_de_pelos TEXT,
	a6 INT,
	explica_tu_respuesta_en_la_frase_pelota_de_plata TEXT,
	a7 INT,
	total_a INT,
	
	--Datos de prueba 2
	PRUEBA_2 TEXT,--==========================================================
	
	--Ejercicio 1
	c1_num_fr INT,
	c1_frase TEXT,
	pregunta1 TEXT,
	c1t TEXT,
	concepto_r_1 TEXT,
	df_1 TEXT,
	c1_1 TEXT,
	c2_1 TEXT,
	c3_1 TEXT,
	criterio_1 TEXT,
	c1 INT,
	
	--Ejercicio 2
	c2_num_fr INT,
	c2_frase TEXT,
	pregunta2 TEXT,
	c2t TEXT,
	concepto_r_2 TEXT,
	df_2 TEXT,
	c1_2 TEXT,
	c2_2 TEXT,
	c3_2 TEXT,
	c4_2 TEXT,
	criterio_2 TEXT,
	c2 INT,
	
	--Ejercicio 3
	c3_num_fr INT,
	c3_frase TEXT,
	pregunta3 TEXT,
	c3t TEXT,
	concepto_r_3 TEXT,
	df_3 TEXT,
	c1_3 TEXT,
	c2_3 TEXT,
	c3_3 TEXT,
	c4_3 TEXT,
	criterio_3 TEXT,
	c3 INT,
	
	--Ejercicio 4
	c4_num_fr INT,
	c4_frase TEXT,
	pregunta4 TEXT,
	c4t TEXT,
	concepto_r_4 TEXT,
	df_4 TEXT,
	c1_4 TEXT,
	c2_4 TEXT,
	c3_4 TEXT,
	c4_4 TEXT,
	criterio_4 TEXT,
	c4 INT,
	
	--Ejercicio 5
	c5_num_fr INT,
	c5_frase TEXT,
	pregunta5 TEXT,
	c5t TEXT,
	concepto_r_5 TEXT,
	df_5 TEXT,
	c1_5 TEXT,
	c2_5 TEXT,
	c3_5 TEXT,
	c4_5 TEXT,
	criterio_5 TEXT,
	c5 INT,
	
	--Ejercicio 6
	c6_num_fr INT,
	c6_frase TEXT,
	pregunta6 TEXT,
	c6t TEXT,
	concepto_r_6 TEXT,
	df_6 TEXT,
	c1_6 TEXT,
	c2_6 TEXT,
	c3_6 TEXT,
	criterio_6 TEXT,
	c6 TEXT,
	
	--Datos de prueba 3
	PRUEBA_3 TEXT,--==========================================================
	
	--Frase 1
	b1__num_fr INT,
	b1_frase TEXT,
	b1 INT,
	es_posible_1 TEXT,
	b1a INT,
	que_significa_1 TEXT,
	b1b INT,
	por_que_crees_que_si_o_no_es_posible_1 TEXT,
	b1c INT,
	b1_ruta TEXT,
	c1_b1 TEXT,
	c2_b1 TEXT,
	c3_b1 TEXT,
	c4_b1 TEXT,
	
	--Frase 2
	b2_num_fr INT,
	b2_frase TEXT,
	b2 INT,
	es_posible_2 TEXT,
	b2a INT,
	que_significa_2 TEXT,
	b2b INT,
	por_que_crees_que_si_o_que_no_es_posible_2 TEXT,
	b2c INT,
	b2_ruta TEXT,
	c1_b2 TEXT,
	c2_b2 TEXT,
	c3_b2 TEXT,
	
	--Frase 3
	b3__num_fr INT,
	b3_frase TEXT,
	b3 INT,
	es_posible_3 TEXT,
	b3a INT,
	que_significa_3 TEXT,
	b3b INT,
	por_que_crees_que_si_o_que_no_es_posible_3 TEXT,
	b3c INT,
	b3_ruta TEXT,
	c1_b3 TEXT,
	c2_b3 TEXT,
	c3_b3 TEXT,
	
	--Frase 4
	b4__num_fr INT,
	b4_frase TEXT,
	b4 INT,
	es_posible_4 TEXT,
	b4a INT,
	que_significa_4 TEXT,
	b4b INT,
	por_que_crees_que_si_o_que_no_es_posible_4 TEXT,
	b4c INT,
	b4_ruta TEXT,
	c1_b4 TEXT,
	c2_b4 TEXT,
	c3_b4 TEXT,
	c4_b4 TEXT,
	
	--Frase 5
	b5__num_fr INT,
	b5_frase TEXT,
	b5 INT,
	es_posible_5 TEXT,
	b5a INT,
	que_significa_5 TEXT,
	b5b INT,
	por_que_crees_que_si_o_que_no_es_posible_5 TEXT,
	b5c INT,
	b5_ruta TEXT,
	c1_b5 TEXT,
	c2_b5 TEXT,
	c3_b5 TEXT,
	c4_b5 TEXT,

	--Frase 6
	b6__num_fr INT,
	b6_frase TEXT,
	b6 INT,
	es_posible_6 TEXT,
	b6a INT,
	que_significa_6 TEXT,
	b6b INT,
	por_que_crees_que_si_o_que_no_es_posible_6 TEXT,
	b6c INT,
	b6_ruta TEXT,
	c1_b6 TEXT,
	c2_b6 TEXT,
	c3_b6 TEXT,

	--Frase 7
	b7__num_fr INT,
	b7_frase TEXT,
	b7 INT,
	es_posible_7 TEXT,
	b7a INT,
	que_significa_7 TEXT,
	b7b INT,
	por_que_crees_que_si_o_que_no_es_posible_7 TEXT,
	b7c INT,
	b7_ruta TEXT,
	c1_b7 TEXT,
	c2_b7 TEXT,
	c3_b7 TEXT,

	--Frase 8
	b8__num_fr INT,
	b8_frase TEXT,
	b8 INT,
	es_posible_8 TEXT,
	b8a INT,
	que_significa_8 TEXT,
	b8b INT,
	por_que_crees_que_si_o_que_no_es_posible_8 TEXT,
	b8c INT,
	b8_ruta TEXT,
	c1_b8 TEXT,
	c2_b8 TEXT,
	
	--Frase 9
	b9__num_fr INT,
	b9_frase TEXT,
	b9 INT,
	es_posible_9 TEXT,
	b9a INT,
	que_significa_9 TEXT,
	b9b INT,
	por_que_crees_que_si_o_que_no_es_posible_9 TEXT,
	b9c INT,
	b9_ruta TEXT,
	c1_b9 TEXT,
	c2_b9 TEXT,
	c3_b9 TEXT,
	
	--Frase 10
	b10__num_fr INT,
	b10_frase TEXT,
	b10 INT,
	es_posible_10 TEXT,
	b10a INT,
	que_significa_10 TEXT,
	b10b INT,
	por_que_crees_que_si_o_que_no_es_posible_10 TEXT,
	b10c INT,
	b10_ruta TEXT,
	c1_b10 TEXT,
	c2_b10 TEXT,
	c3_b10 TEXT,
	
	--Frase 11
	b11__num_fr INT,
	b11_frase TEXT,
	b11 INT,
	es_posible_11 TEXT,
	b11a INT,
	que_significa_11 TEXT,
	b11b INT,
	por_que_crees_que_si_o_que_no_es_posible_11 TEXT,
	b11c INT,
	b11_ruta TEXT,
	c1_b11 TEXT,
	c2_b11 TEXT,
	c3_b11 TEXT,
	
	--Frase 12
	b12__num_fr INT,
	b12_frase TEXT,
	b12 INT,
	es_posible_12 TEXT,
	b12a INT,
	que_significa_12 TEXT,
	b12b INT,
	por_que_crees_que_si_o_que_no_es_posible_12 TEXT,
	b12c INT,
	b12_ruta TEXT,
	c1_b12 TEXT,
	c2_b12 TEXT,
	c3_b12 TEXT,
	
	--Frase 13
	b13__num_fr INT,
	b13_frase TEXT,
	b13 INT,
	es_posible_13 TEXT,
	b13a INT,
	que_significa_13 TEXT,
	b13b INT,
	por_que_crees_que_si_o_que_no_es_posible_13 TEXT,
	b13c INT,
	b13_ruta TEXT,
	c1_b13 TEXT,
	c2_b13 TEXT,
	c3_b13 TEXT,
	
	--Frase 14
	b14__num_fr INT,
	b14_frase TEXT,
	b14 INT,
	es_posible_14 TEXT,
	b14a INT,
	que_significa_14 TEXT,
	b14b INT,
	por_que_crees_que_si_o_que_no_es_posible_14 TEXT,
	b14c INT,
	b14_ruta TEXT,
	c1_b14 TEXT,
	c2_b14 TEXT,
	
	--Frase 15
	b15__num_fr INT,
	b15_frase TEXT,
	b15 INT,
	es_posible_15 TEXT,
	b15a INT,
	que_significa_15 TEXT,
	b15b INT,
	por_que_crees_que_si_o_que_no_es_posible_15 TEXT,
	b15c INT,
	b15_ruta TEXT,
	c1_b15 TEXT,
	c2_b15 TEXT,
	
	--Frase 16
	b16__num_fr INT,
	b16_frase TEXT,
	b16 INT,
	es_posible_16 TEXT,
	b16a INT,
	que_significa_16 TEXT,
	b16b INT,
	por_que_crees_que_si_o_que_no_es_posible_16 TEXT,
	b16c INT,
	b16_ruta TEXT,
	c1_b16 TEXT,
	c2_b16 TEXT,
	
	--Frase 17
	b17__num_fr INT,
	b17_frase TEXT,
	b17 INT,
	es_posible_17 TEXT,
	b17a INT,
	que_significa_17 TEXT,
	b17b INT,
	por_que_crees_que_si_o_que_no_es_posible_17 TEXT,
	b17c INT,
	b17_ruta TEXT,
	c1_b17 TEXT,
	c2_b17 TEXT,
	
	--Frase 18
	b18__num_fr INT,
	b18_frase TEXT,
	b18 INT,
	es_posible_18 TEXT,
	b18a INT,
	que_significa_18 TEXT,
	b18b INT,
	por_que_crees_que_si_o_que_no_es_posible_18 TEXT,
	b18c INT,
	b18_ruta TEXT,
	c1_b18 TEXT,
	c2_b18 TEXT,
	c3_b18 TEXT,
	califico TEXT,
	
	--Datos de prueba 4
	PRUEBA_4 TEXT,--==========================================================
	d_tipo INT,
	clave_1 TEXT,
    d1_tipo TEXT,
    simon_ha_estado_caminando_en_la_nieve_por_horas_sus_pies TEXT,
    d1 TEXT, -- tiene abcd o numeros
    clave_2 TEXT,
    d2_tipo TEXT,
    el_arbol_de_mi_jardin_ha_crecido_mucho_este_ano TEXT,
    d2 TEXT, -- tiene abcd o numeros

    clave_3 TEXT,
    d3_tipo TEXT,
    mi_mama_dejo_el_pan_afuera_toda_la_noche_en_la_manana TEXT,
    d3 TEXT, -- tiene abcd o numeros

    clave_4 TEXT,
    d4_tipo TEXT,
    mi_amigo_de_la_escuela_siempre_me_protege_de_los_bravucones_el TEXT,
    d4 TEXT, -- tiene abcd o numeros
    
    clave_5 TEXT,
    d5_tipo TEXT,
    laura_habla_tan_suavemente_que_apenas_puedes_oirla_ella TEXT,
    d5 TEXT, -- tiene abcd o numeros
    
    clave_6 TEXT,
    d6_tipo TEXT,
    jeny_siempre_saca_buenas_calificaciones_en_sus_examenes_ella_es TEXT,
    d6 TEXT, -- tiene abcd o numeros
    
    clave_7 TEXT,
    d7_tipo TEXT,
    mi_papa_estaba_muy_enojado_cuando_llegue_tarde_a_la_casa_el TEXT,
    d7 TEXT, -- tiene abcd o numeros
    
    clave_8 TEXT,
    d8_tipo TEXT,
    peter_puede_levantar_cosas_muy_pesadas_sin_ningun_problema_el TEXT,
    d8 TEXT, -- tiene abcd o numeros
    
    clave_9 TEXT,
    d9_tipo TEXT,
    nuestra_nueva_escuela_es_muy_grande_y_yo_siempre_me_pierdo TEXT,
    d9 TEXT, -- tiene abcd o numeros
    
    clave_10 TEXT,
    d10_tipo TEXT,
    las_unas_largas_de_july_estan_pintadas_de_rojo_y_dorado TEXT,
    d10 TEXT, -- tiene abcd o numeros
    
    clave_11 TEXT,
    d11_tipo TEXT,
    luis_siempre_esta_contento_y_eso_hace_sentir_bien_a_los_demas_e TEXT,
    d11 TEXT, -- tiene abcd o numeros
    
    clave_12 TEXT,
    d12_tipo TEXT,
    paty_tiene_el_pelo_muy_largo_y_liso_su_cabello TEXT,
    d12 TEXT, -- tiene abcd o numeros
    
    clave_13 TEXT,
    d13_tipo TEXT,
    joe_paso_mucho_tiempo_en_la_alberca_el TEXT,
    d13 TEXT, -- tiene abcd o numeros
    
    clave_14 TEXT,
    d14_tipo TEXT,
    el_nuevo_perro_de_sam_es_muy_grande TEXT,
    d14 TEXT, -- tiene abcd o numeros
    
    clave_15 TEXT,
    d15_tipo TEXT,
    luisa_ha_estado_gritando_y_llorando_por_horas_ella TEXT,
    d15 TEXT, -- tiene abcd o numeros
    
    clave_16 TEXT,
    d16_tipo TEXT,
    la_calefaccion_ha_estado_prendida_por_horas_y_la_habitacion TEXT,
    d16 TEXT, -- tiene abcd o numeros
    
    clave_17 TEXT,
    d17_tipo TEXT,
    kate_tiene_una_linda_cara_y_bonitos_ojos_ella TEXT,
    d17 TEXT, -- tiene abcd o numeros
    
    clave_18 TEXT,
    d18_tipo TEXT,
    julian_esta_escondido_detras_del_arbol_sin_moverse_el_es TEXT,
    d18 TEXT, -- tiene abcd o numeros
    
    total_d INT

);
	