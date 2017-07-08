<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<?php

	$bdd = mysql_connect('mysql.hostinger.fr', 'u282906387_coni', 'wfytyjqj');
	mysql_select_db('u282906387_rerc',$bdd); 
	
	//recup du num du dernier rc
	
	$querymax = mysql_query('SELECT MAX(Num) AS MAXRE FROM re');
	$DEBUT = mysql_fetch_assoc($querymax);
	$num = $DEBUT['MAXRE'];
	
	$offset = isset($_GET['offset']) ? (int) $_GET['offset'] : 0;
	
	$trigger_stop=0;
	$inc = $num+1+$offset;
	
	while ($trigger_stop < 20){	
		//incrémentation et passage en md5
			$hash2 = md5($inc);
			$url ='http://game.desert-operations.fr/world1/spionageReport.php?code='.$hash2;
			
		//génération et recup du DOM de l'url
			$dom = new DOMDocument();
			libxml_use_internal_errors(true);
			$dom->loadHTMLFile($url);
			$p =  $dom->getElementsByTagName("p")->item(0)->nodeValue;
			
		if (!is_null($p))
		{	
			$trigger_stop=0;
			
		// traitement du DOM 	
						
			//$pattern = '/- [A-Za-zéô ]+$/';
			//preg_match($pattern, $titre, $matches);
			$subject = $dom->getElementById('battleOverviewPercentualLosses')->getElementsByTagName("table")->item(0)->getElementsByTagName("td")->item(4)->nodeValue;
			$accent = Array("é","ô", "- ");
			$Saccent = Array("e","o", "");
			$Type = str_replace($accent, $Saccent, $subject);
			
			//$patternplayer = '/[A-Za-z0-9-_]+Pr/';
			//preg_match_all($patternplayer, $player, $resultat);
			//$string = $resultat[0][0];
			//$def = substr($string,0,strlen($string)-2);
			$def = $dom->getElementById('battleOverviewLooserName')->nodeValue;
			
			//$patternwin = '/[0-9.]+ %$/m';
			//preg_match($patternwin, $p, $win);
			$preci = $dom->getElementById('battleOverviewPercentualLosses')->getElementsByTagName("table")->item(0)->getElementsByTagName("td")->item(14)->nodeValue;
			
			$date2 = $dom->getElementById('battleReportHeadlineTimeString')->nodeValue;
			$date = DateTime::createFromFormat('j.m.y H:i:s', $date2);
			$date = date_format($date, 'Y-m-j H:i:s');

		//ajout dans la table	
			$rqt = 'INSERT INTO re (Num, Md5, Def, Date, Type, Prec) 
					VALUES (
					'.$inc.', 
					"'.$hash2.'", 
					"'.$def.'",
					"'.$date.'",
					"'.$Type.'",
					"'.$preci.'")';
			mysql_query($rqt);
		
			$inc++;
		}
		else
		{
			$trigger_stop++;	
			$inc++;
		}	
	}
	mysql_close();

?>