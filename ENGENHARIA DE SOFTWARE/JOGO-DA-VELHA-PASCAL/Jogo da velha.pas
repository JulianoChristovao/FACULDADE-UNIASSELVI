Program Jogo_da_Velha ;
//Elabore um algoritmo que utilize uma matriz 3 x 3 para simular o jogo da velha, 
//apresentando a situação do jogo a cada rodada

const
	tamanho = 3;
var
	mat_jog_velha : array[1..tamanho, 1..tamanho] of string;
	jogador, i, j, k : integer;
	jogada : boolean;
	

	//procedimento para jogada
	procedure proced_realizar_jogada();
	var
		posicao : boolean = true;
	begin
		if jogador = 1 then
		begin
			while posicao = true do
			begin
				writeln();
				writeln('Vez do jogador 1: ');
				write('Digite qual linha: ');
				readln(i);
				write('Digite qual coluna: ');
				readln(j);
				if (i <= tamanho) and (j <= tamanho) then
				begin
					if (mat_jog_velha[i, j] = ' ') then
					begin       
						posicao := false;
						jogador := 2;
						mat_jog_velha[i, j] := '1';
					end
					else
					begin
						writeln('Posição já jogada, tente novamente!!!');
						writeln();
					end
				end
				else
				begin
					writeln('Posição incorreta, tente novamente!!!');
					writeln();
				end;
			end;
		end;
		
		//jogada do jogador 2
		if jogador = 2 then
		begin
			while posicao = true do
			begin
				writeln();
				writeln('Vez do jogador 2: ');
				write('Digite qual linha: ');
				readln(i);
				write('Digite qual coluna: ');
				readln(j);
				if (i <= tamanho) and (j <= tamanho) then
				begin
					if (mat_jog_velha[i, j] = ' ') then
					begin       
						posicao := false;
						jogador := 1;
						mat_jog_velha[i, j] := '2';
					end
					else
					begin
						writeln('Posição já jogada, tente novamente!!!');
						writeln();
					end
				end
				else
				begin
					writeln('Posição incorreta, tente novamente!!!');
					writeln();
				end;
			end;
			posicao := true;	
		end;
	end;
	
		
	procedure proced_check_jogada();
	var
	vencedor : integer;
	begin	
		//check jogada horizontal
		for i := 1 to tamanho do
		begin	
			if (mat_jog_velha[i, 1] = '1') and (mat_jog_velha[i, 2] = '1') and (mat_jog_velha[i, 3] = '1') then
			begin
				vencedor := 1;
				writeln();
				writeln('Jogador 1 venceu');
				writeln();
				jogada := false;
				exit;
			end
			else if (mat_jog_velha[i, 1] = '2') and (mat_jog_velha[i, 2] = '2') and (mat_jog_velha[i, 3] = '2') then	
			begin
				vencedor := 2;
				writeln();
				writeln('Jogador 2 venceu');
				writeln();
				jogada := false;
				exit;
			end;
		end; 

		//check jogada verical
	  for i := 1 to tamanho do
		begin	
			if (mat_jog_velha[1, i] = '1') and (mat_jog_velha[2, i] = '1') and (mat_jog_velha[3, i] = '1') then
			begin
				vencedor := 1;
				writeln();
				writeln('Jogador 1 venceu');
				writeln();
				jogada := false;
				exit;
			end
			else if (mat_jog_velha[1, i] = '2') and (mat_jog_velha[2, i] = '2') and (mat_jog_velha[3, i] = '2') then	
			begin
				vencedor := 2;
				writeln();
				writeln('Jogador 2 venceu');
				writeln();
				jogada := false;
				exit;
			end;
		end; 
		
		//check diagonal
		if (mat_jog_velha[1, 1] = '1') and (mat_jog_velha[2, 2] = '1') and (mat_jog_velha[3, 3] = '1') then
		begin
			vencedor := 1;
			writeln();
			writeln('Jogador 1 venceu!!!');
			writeln();
			jogada := false;
			exit;
		end
		else if (mat_jog_velha[1, 3] = '2') and (mat_jog_velha[2, 2] = '2') and (mat_jog_velha[3, 1] = '2') then	
		begin
			vencedor := 2;
			writeln();
			writeln('Jogador 2 venceu!!!');
			writeln();
			jogada := false;
			exit;
		end;
		
		//check se todos estão preenchidos
		for i := 1 to tamanho do
		begin
			for j := 1 to tamanho do
			begin
				if mat_jog_velha[i, j] = ' ' then
					exit
			end;
		end;
		writeln();
		writeln('Ninguem ganhou!!!');
		writeln();
		jogada := false;
	end;
	
	//Procedimento para mostrar o status do jogo
	procedure proced_mostra_jogo();
	begin
		for i := 1 to tamanho do
		begin
			write('| ');
			for j := 1 to tamanho do
			begin
				
				write(mat_jog_velha[i, j], ' | ');
			end;
			writeln();
			if i < tamanho then
			begin
				writeln('-------------');
			end;
		end;
	end;
	
// Programa principal
Begin
	while true do
	begin
		for i := 1 to tamanho do
		begin
			for j := 1 to tamanho do
			begin
				mat_jog_velha[i, j] := ' ';
			end;
		end;
		writeln('Bem vindo ao jogo da velha, vamos iniciar!!!');
		writeln();
		proced_mostra_jogo();
		jogada := true;
		jogador := 1;
		while jogada = true do
		begin	
			proced_realizar_jogada();
			proced_check_jogada();
			proced_mostra_jogo();
		end;
		writeln();
	end;  
End.