/* 
 * Copyright 2014-5 ClinRisk Ltd.
 * 
 * This file is part of QRISK2-2015 (http://qrisk.org, http://qrisk.org/QRISK2-2015-lgpl-source.tgz).
 * 
 * QRISK2-2015 is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * QRISK2-2015 is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public License
 * along with QRISK2-2015.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Additional terms
 *
 * The following disclaimer must be held together with any risk score score generated by this code.  
 * If the score is displayed, then this disclaimer must be displayed or otherwise be made easily accessible, e.g. by a prominent link alongside it.
 *   The initial version of this file, to be found at http://qrisk.org/QRISK2-2015-lgpl-source.tgz, faithfully implements QRISK2-2015.
 *   ClinRisk Ltd. have released this code under the GNU Lesser General Public License to enable others to implement the algorithm faithfully.
 *   However, the nature of the GNU Lesser General Public License is such that we cannot prevent, for example, someone accidentally
 *   altering the coefficients, getting the inputs wrong, or just poor programming.
 *   ClinRisk Ltd. stress, therefore, that it is the responsibility of the end user to check that the source that 
 *   they receive produces the same results as the original code posted at http://qrisk.org/QRISK2-2015-lgpl-source.tgz.
 *   Inaccurate implementations of risk scores can lead to wrong patients being given the wrong treatment.
 * 
 * End of additional terms
 */

#include <math.h>
#include <string.h>
#include <Python.h>

static PyObject* calcFemRaw(PyObject* self, PyObject* args){
	int surv = 10;
	int age, b_AF, b_ra, b_renal, b_treatedhyp, b_type1, b_type2, ethrisk, fh_cvd, smoke_cat;
	double bmi, rati, sbp, town;

	if (!PyArg_ParseTuple(args, "iiiiiiidiiddid", &age, &b_AF, &b_ra, &b_renal, &b_treatedhyp, &b_type1, &b_type2, &bmi, &ethrisk, &fh_cvd, &rati, &sbp, &smoke_cat, &town)){
	    return NULL;
	}

	double survivor[16] = {
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0,
		0.989747583866119,
		0,
		0,
		0,
		0,
		0
	};

	/* The conditional arrays */

	double Iethrisk[10] = {
		0,
		0,
		0.2574099349831925900000000,
		0.6129795430571779400000000,
		0.3362159841669621300000000,
		0.1512517303224336400000000,
		-0.1794156259657768100000000,
		-0.3503423610057745400000000,
		-0.2778372483233216800000000,
		-0.1592734122665366000000000
	};
	double Ismoke[5] = {
		0,
		0.2119377108760385200000000,
		0.6618634379685941500000000,
		0.7570714587132305600000000,
		0.9496298251457036000000000
	};

	/* Applying the fractional polynomial transforms */
	/* (which includes scaling)                      */

	double dage = age;
	dage=dage/10;
	double age_2 = dage;
	double age_1 = pow(dage,.5);
	double dbmi = bmi;
	dbmi=dbmi/10;
	double bmi_2 = pow(dbmi,-2)*log(dbmi);
	double bmi_1 = pow(dbmi,-2);

	/* Centring the continuous variables */

	age_1 = age_1 - 2.086397409439087;
	age_2 = age_2 - 4.353054523468018;
	bmi_1 = bmi_1 - 0.152244374155998;
	bmi_2 = bmi_2 - 0.143282383680344;
	rati = rati - 3.506655454635620;
	sbp = sbp - 125.040039062500000;
	town = town - 0.416743695735931;

	/* Start of Sum */
	double a=0;

	/* The conditional sums */

	a += Iethrisk[ethrisk];
	a += Ismoke[smoke_cat];

	/* Sum from continuous values */

	a += age_1 * 4.4417863976316578000000000;
	a += age_2 * 0.0281637210672999180000000;
	a += bmi_1 * 0.8942365304710663300000000;
	a += bmi_2 * -6.5748047596104335000000000;
	a += rati * 0.1433900561621420900000000;
	a += sbp * 0.0128971795843613720000000;
	a += town * 0.0664772630011438850000000;

	/* Sum from boolean values */

	a += b_AF * 1.6284780236484424000000000;
	a += b_ra * 0.2901233104088770700000000;
	a += b_renal * 1.0043796680368302000000000;
	a += b_treatedhyp * 0.6180430562788129500000000;
	a += b_type1 * 1.8400348250874599000000000;
	a += b_type2 * 1.1711626412196512000000000;
	a += fh_cvd * 0.5147261203665195500000000;

	/* Sum from interaction terms */

	a += age_1 * (smoke_cat==1) * 0.7464406144391666500000000;
	a += age_1 * (smoke_cat==2) * 0.2568541711879666600000000;
	a += age_1 * (smoke_cat==3) * -1.5452226707866523000000000;
	a += age_1 * (smoke_cat==4) * -1.7113013709043405000000000;
	a += age_1 * b_AF * -7.0177986441269269000000000;
	a += age_1 * b_renal * -2.9684019256454390000000000;
	a += age_1 * b_treatedhyp * -4.2219906452967848000000000;
	a += age_1 * b_type1 * 1.6835769546040080000000000;
	a += age_1 * b_type2 * -2.9371798540034648000000000;
	a += age_1 * bmi_1 * 0.1797196207044682300000000;
	a += age_1 * bmi_2 * 40.2428166760658140000000000;
	a += age_1 * fh_cvd * 0.1439979240753906700000000;
	a += age_1 * sbp * -0.0362575233899774460000000;
	a += age_1 * town * 0.3735138031433442600000000;
	a += age_2 * (smoke_cat==1) * -0.1927057741748231000000000;
	a += age_2 * (smoke_cat==2) * -0.1526965063458932700000000;
	a += age_2 * (smoke_cat==3) * 0.2313563976521429400000000;
	a += age_2 * (smoke_cat==4) * 0.2307165013868296700000000;
	a += age_2 * b_AF * 1.1395776028337732000000000;
	a += age_2 * b_renal * 0.4356963208330940600000000;
	a += age_2 * b_treatedhyp * 0.7265947108887239600000000;
	a += age_2 * b_type1 * -0.6320977766275653900000000;
	a += age_2 * b_type2 * 0.4023270434871086800000000;
	a += age_2 * bmi_1 * 0.1319276622711877700000000;
	a += age_2 * bmi_2 * -7.3211322435546409000000000;
	a += age_2 * fh_cvd * -0.1330260018273720400000000;
	a += age_2 * sbp * 0.0045842850495397955000000;
	a += age_2 * town * -0.0952370300845990780000000;

	/* Calculate the score itself */
	double score = 100.0 * (1 - pow(survivor[surv], exp(a)) );
	//return score;
	return PyFloat_FromDouble(score);
}


/*
 * Bind Python function names to our C functions
 */
static PyMethodDef py_qriskMethods[] = {
  {"calcFemRaw", calcFemRaw, METH_VARARGS},
  {NULL, NULL}
};

/*
 * Python calls this to let us initialize our module
 */
void initpy_qrisk()
{
  (void) Py_InitModule("py_qrisk", py_qriskMethods);
}