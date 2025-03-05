Program Jogo_Batalha_Naval ;
//Elabore um algoritmo que utilize uma matriz 5 x 5 para 
//simular o jogo de batalha naval, apresentando a situação 
//do jogo a cada rodada
const
	tamanho = 5;
	embarcacao = 3;
var
	mat_jogador_1, mat_jogador_2 : array[1..tamanho, 1..tamanho] of string;
	i, x, y, jogador : integer;
	jogar: boolean = false;
	contador_jog_1, contador_jog_2 : integer = embarcacao;

	// Procedimento para montar o jogo
	procedure proced_montar();
	var
		montagem: boolean;
	
	//________________inicio_________________ 
	//subrotina para atualixar o jogo a cada posicionamento namontagem
	procedure proced_mostra_jogo_proced_montar();
	begin
	// Mostra jogo do jogador 1 no procedimento de montar
		writeln('Mapa do jogador 1');
		for x := 1 to tamanho do
		begin
			write('| ');
			for y := 1 to tamanho do
			begin	
				write(mat_jogador_1[x, y], ' | ');
			end;
			writeln();
			if x < tamanho then
			begin
				writeln('---------------------');
			end;
		end;
		writeln();
		// Mostra jogo do jogador 1 no procedimento de montar
		writeln('Mapa do jogador 2');
		for x := 1 to tamanho do
		begin
			write('| ');
			for y := 1 to tamanho do
			begin	
				write(mat_jogador_2[x, y], ' | ');
			end;
			writeln();
			if x < tamanho then
			begin
				writeln('---------------------');
			end;
		end;
	end;  
		// ___________________fim____________________
	begin
		//montagem do jogador 1
		montagem := true;
		for i := 1 to embarcacao do
		begin
			writeln();
			while montagem = true do
			begin
				writeln('Jogador 1');
				write('Digite a posição da ', i, 'ª na embarcação na posição X: ');
				readln(x);
				write('Digite a posição da ', i, 'ª  na embarcação na posição Y: ');
				readln(y);
				if (x <= tamanho) and (y <= tamanho) then
				begin
					if mat_jogador_1[x, y] = ' ' then
					begin
						mat_jogador_1[x, y] := 'O';
						montagem := false;
					end
					else
					begin
					  writeln('Posição já ocupada, tente novamente');
					end;
				end
				else
				begin
					writeln('Posiçao incorreta, tente novamente.')
				end;
			end;
			montagem := true;
			proced_mostra_jogo_proced_montar();
		end;
		//montagem do jogador 2
		montagem := true;
		jogador := 1;
		for i := 1 to embarcacao do
		begin
			writeln();
			while montagem = true do
			begin
				writeln('Jogador 2');
				write('Digite a posição da ', i, 'ª na embarcação na posição X: ');
				readln(x);
				write('Digite a posição da ', i, 'ª  na embarcação na posição Y: ');
				readln(y);
				if (x <= tamanho) and (y <= tamanho) then
				begin
					if mat_jogador_2[x, y] = ' ' then
					begin
						mat_jogador_2[x, y] := 'O';
						montagem := false;
					end
					else
					begin
					  writeln('Posição já ocupada, tente novamente');
					end;
				end
				else
				begin
					writeln('Posiçao incorreta, tente novamente.')
				end;
			end;
			montagem := true;
			proced_mostra_jogo_proced_montar();
		end;
	end;
		
	//Procedimento para mostrar o status do jogo
	procedure proced_mostra_jogo();
	begin
		// Mostra jogo do jogador 1
		writeln('Mapa do jogador 1');
		for x := 1 to tamanho do
		begin
			write('| ');
			for y := 1 to tamanho do
			begin				
				write(mat_jogador_1[x, y], ' | ');
			end;
			writeln();
			if x < tamanho then
			begin
				writeln('---------------------');
			end;
		end;
		writeln();
		
		// Mostra jogo do jogador 2
		writeln('Mapa do jogador 2');
		for x := 1 to tamanho do
		begin
			write('| ');
			for y := 1 to tamanho do
			begin
				write(mat_jogador_2[x, y], ' | ');
			end;
			writeln();
			if x < tamanho then
			begin
				writeln('---------------------');
			end;
		end;
	end; 
	     
	// Procedimento para jogar
	procedure proced_jogar();
	var
		jogada : boolean = true;
	//jogada do jogador 1
	begin
		if jogador = 1 then
		begin
			while jogada = true do
			begin
				writeln('Jogador 1');
				write('Digite a posição do alvo na posição X: ');
				readln(x);
				write('Digite a posição do alvo na posição Y: ');
				readln(y);
				if (x <= tamanho) and (y <= tamanho) then
				begin
					if mat_jogador_2[x, y] = ' ' then
					begin
						mat_jogador_2[x, y] := 'X';
						jogada := false;
						writeln('Você não acertou!!!');
					end
					else if mat_jogador_2[x, y] <> 'X' then
					begin
						mat_jogador_2[x, y] := '#';
						jogada := false;
						writeln('Você destruiu a embarcação!!!');
						contador_jog_2 := contador_jog_2 - 1;
					end
					else
					begin
						writeln('Posição já utilizada, tente novamente');
					end;
				end
				else
				begin
					writeln('Posiçao incorreta, tente novamente.')
				end;
			end;
			jogada := true;	
		end;
		
		if jogador = 2 then
		begin
			while jogada = true do
			begin
				writeln('Jogador 2');
				write('Digite a posição do alvo na posição X: ');
				readln(x);
				write('Digite a posição do alvo na posição Y: ');
				readln(y);
				if (x <= tamanho) and (y <= tamanho) then
				begin
					if mat_jogador_1[x, y] = ' ' then
					begin
						mat_jogador_1[x, y] := 'X';
						jogada := false;
						writeln('Você não acertou!!!');
					end
					else if mat_jogador_1[x, y] <> 'X' then
					begin
						mat_jogador_1[x, y] := '#';
						jogada := false;
						writeln('Você destruiu a embarcação!!!');
						contador_jog_1 := contador_jog_1 - 1;
					end
					else
					begin
						writeln('Posição já utilizada, tente novamente');
					end;
				end
				else
				begin
					writeln('Posiçao incorreta, tente novamente.')
				end;
			end;
			jogada := true;	
		end;
		if jogador = 1 then
			begin
				jogador := 2;
			end
			else
			begin
				jogador := 1;
			end;	
	end;	
	 
// Programa principal
Begin
	//inicializar o jogo
	for x := 1 to tamanho do
		begin
			for y := 1 to tamanho do
			begin
				mat_jogador_1[x, y] := ' ';
			end;
		end;
		
		for x := 1 to tamanho do
		begin
			for y := 1 to tamanho do
			begin
				mat_jogador_2[x, y] := ' ';
			end;
		end;
	jogar := true;
	proced_mostra_jogo();	
	proced_montar();
	proced_mostra_jogo();
	
	//jogar
	while jogar = true do
	begin
		proced_jogar();
		proced_mostra_jogo();
		if contador_jog_1 = 0 then
		begin
			jogar := false;
			jogador := 1;
		end
		else if contador_jog_2 = 0 then
		begin
			jogar := false;
			jogador := 2;
		end;
	end;
	writeln('Jogador ', jogador, ' venceu!!!');
		  
End.