// Generated from /home/curso/SDT-project/SDT-project/src/main/python/compiladores.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link compiladoresParser}.
 */
public interface compiladoresListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(compiladoresParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(compiladoresParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#instrucciones}.
	 * @param ctx the parse tree
	 */
	void enterInstrucciones(compiladoresParser.InstruccionesContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#instrucciones}.
	 * @param ctx the parse tree
	 */
	void exitInstrucciones(compiladoresParser.InstruccionesContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterInstruccion(compiladoresParser.InstruccionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitInstruccion(compiladoresParser.InstruccionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracion(compiladoresParser.DeclaracionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracion(compiladoresParser.DeclaracionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#definicion}.
	 * @param ctx the parse tree
	 */
	void enterDefinicion(compiladoresParser.DefinicionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#definicion}.
	 * @param ctx the parse tree
	 */
	void exitDefinicion(compiladoresParser.DefinicionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#bloque}.
	 * @param ctx the parse tree
	 */
	void enterBloque(compiladoresParser.BloqueContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#bloque}.
	 * @param ctx the parse tree
	 */
	void exitBloque(compiladoresParser.BloqueContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(compiladoresParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(compiladoresParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#lista_var}.
	 * @param ctx the parse tree
	 */
	void enterLista_var(compiladoresParser.Lista_varContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#lista_var}.
	 * @param ctx the parse tree
	 */
	void exitLista_var(compiladoresParser.Lista_varContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#while_stmt}.
	 * @param ctx the parse tree
	 */
	void enterWhile_stmt(compiladoresParser.While_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#while_stmt}.
	 * @param ctx the parse tree
	 */
	void exitWhile_stmt(compiladoresParser.While_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#ret}.
	 * @param ctx the parse tree
	 */
	void enterRet(compiladoresParser.RetContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#ret}.
	 * @param ctx the parse tree
	 */
	void exitRet(compiladoresParser.RetContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void enterIf_stmt(compiladoresParser.If_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void exitIf_stmt(compiladoresParser.If_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#for_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFor_stmt(compiladoresParser.For_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#for_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFor_stmt(compiladoresParser.For_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#opar}.
	 * @param ctx the parse tree
	 */
	void enterOpar(compiladoresParser.OparContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#opar}.
	 * @param ctx the parse tree
	 */
	void exitOpar(compiladoresParser.OparContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#logicoperators}.
	 * @param ctx the parse tree
	 */
	void enterLogicoperators(compiladoresParser.LogicoperatorsContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#logicoperators}.
	 * @param ctx the parse tree
	 */
	void exitLogicoperators(compiladoresParser.LogicoperatorsContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#oplo}.
	 * @param ctx the parse tree
	 */
	void enterOplo(compiladoresParser.OploContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#oplo}.
	 * @param ctx the parse tree
	 */
	void exitOplo(compiladoresParser.OploContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#logexpression}.
	 * @param ctx the parse tree
	 */
	void enterLogexpression(compiladoresParser.LogexpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#logexpression}.
	 * @param ctx the parse tree
	 */
	void exitLogexpression(compiladoresParser.LogexpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#primelogexp}.
	 * @param ctx the parse tree
	 */
	void enterPrimelogexp(compiladoresParser.PrimelogexpContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#primelogexp}.
	 * @param ctx the parse tree
	 */
	void exitPrimelogexp(compiladoresParser.PrimelogexpContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#logterm}.
	 * @param ctx the parse tree
	 */
	void enterLogterm(compiladoresParser.LogtermContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#logterm}.
	 * @param ctx the parse tree
	 */
	void exitLogterm(compiladoresParser.LogtermContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#primelogterm}.
	 * @param ctx the parse tree
	 */
	void enterPrimelogterm(compiladoresParser.PrimelogtermContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#primelogterm}.
	 * @param ctx the parse tree
	 */
	void exitPrimelogterm(compiladoresParser.PrimelogtermContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#logfactor}.
	 * @param ctx the parse tree
	 */
	void enterLogfactor(compiladoresParser.LogfactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#logfactor}.
	 * @param ctx the parse tree
	 */
	void exitLogfactor(compiladoresParser.LogfactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#comp}.
	 * @param ctx the parse tree
	 */
	void enterComp(compiladoresParser.CompContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#comp}.
	 * @param ctx the parse tree
	 */
	void exitComp(compiladoresParser.CompContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(compiladoresParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(compiladoresParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#primeexp}.
	 * @param ctx the parse tree
	 */
	void enterPrimeexp(compiladoresParser.PrimeexpContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#primeexp}.
	 * @param ctx the parse tree
	 */
	void exitPrimeexp(compiladoresParser.PrimeexpContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(compiladoresParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(compiladoresParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#primeterm}.
	 * @param ctx the parse tree
	 */
	void enterPrimeterm(compiladoresParser.PrimetermContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#primeterm}.
	 * @param ctx the parse tree
	 */
	void exitPrimeterm(compiladoresParser.PrimetermContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(compiladoresParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(compiladoresParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#functcall}.
	 * @param ctx the parse tree
	 */
	void enterFunctcall(compiladoresParser.FunctcallContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#functcall}.
	 * @param ctx the parse tree
	 */
	void exitFunctcall(compiladoresParser.FunctcallContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#tdata}.
	 * @param ctx the parse tree
	 */
	void enterTdata(compiladoresParser.TdataContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#tdata}.
	 * @param ctx the parse tree
	 */
	void exitTdata(compiladoresParser.TdataContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#functprototype}.
	 * @param ctx the parse tree
	 */
	void enterFunctprototype(compiladoresParser.FunctprototypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#functprototype}.
	 * @param ctx the parse tree
	 */
	void exitFunctprototype(compiladoresParser.FunctprototypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#args}.
	 * @param ctx the parse tree
	 */
	void enterArgs(compiladoresParser.ArgsContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#args}.
	 * @param ctx the parse tree
	 */
	void exitArgs(compiladoresParser.ArgsContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#list_args}.
	 * @param ctx the parse tree
	 */
	void enterList_args(compiladoresParser.List_argsContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#list_args}.
	 * @param ctx the parse tree
	 */
	void exitList_args(compiladoresParser.List_argsContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#functdef}.
	 * @param ctx the parse tree
	 */
	void enterFunctdef(compiladoresParser.FunctdefContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#functdef}.
	 * @param ctx the parse tree
	 */
	void exitFunctdef(compiladoresParser.FunctdefContext ctx);
}