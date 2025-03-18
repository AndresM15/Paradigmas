// Generated from c://Users//salaz//Downloads//InterpreteParadigmasTacticas//TaticBoard.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class TaticBoardParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, INT=12, WS=13;
	public static final int
		RULE_tactic = 0, RULE_action = 1, RULE_playerAction = 2, RULE_moveAction = 3, 
		RULE_passAction = 4, RULE_shootAction = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"tactic", "action", "playerAction", "moveAction", "passAction", "shootAction"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Tactic'", "'{'", "'}'", "'player'", "'('", "')'", "'move'", "','", 
			"'pass'", "'shoot'", "'goal'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"INT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "TaticBoard.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public TaticBoardParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TacticContext extends ParserRuleContext {
		public List<ActionContext> action() {
			return getRuleContexts(ActionContext.class);
		}
		public ActionContext action(int i) {
			return getRuleContext(ActionContext.class,i);
		}
		public TacticContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tactic; }
	}

	public final TacticContext tactic() throws RecognitionException {
		TacticContext _localctx = new TacticContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_tactic);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(12);
			match(T__0);
			setState(13);
			match(T__1);
			setState(15); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(14);
				action();
				}
				}
				setState(17); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__3 );
			setState(19);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ActionContext extends ParserRuleContext {
		public PlayerActionContext playerAction() {
			return getRuleContext(PlayerActionContext.class,0);
		}
		public ActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_action; }
	}

	public final ActionContext action() throws RecognitionException {
		ActionContext _localctx = new ActionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_action);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(21);
			playerAction();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PlayerActionContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(TaticBoardParser.INT, 0); }
		public MoveActionContext moveAction() {
			return getRuleContext(MoveActionContext.class,0);
		}
		public PassActionContext passAction() {
			return getRuleContext(PassActionContext.class,0);
		}
		public ShootActionContext shootAction() {
			return getRuleContext(ShootActionContext.class,0);
		}
		public PlayerActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_playerAction; }
	}

	public final PlayerActionContext playerAction() throws RecognitionException {
		PlayerActionContext _localctx = new PlayerActionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_playerAction);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(23);
			match(T__3);
			setState(24);
			match(T__4);
			setState(25);
			match(INT);
			setState(26);
			match(T__5);
			setState(30);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__6:
				{
				setState(27);
				moveAction();
				}
				break;
			case T__8:
				{
				setState(28);
				passAction();
				}
				break;
			case T__9:
				{
				setState(29);
				shootAction();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MoveActionContext extends ParserRuleContext {
		public List<TerminalNode> INT() { return getTokens(TaticBoardParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(TaticBoardParser.INT, i);
		}
		public MoveActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_moveAction; }
	}

	public final MoveActionContext moveAction() throws RecognitionException {
		MoveActionContext _localctx = new MoveActionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_moveAction);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			match(T__6);
			setState(33);
			match(T__4);
			setState(34);
			match(INT);
			setState(35);
			match(T__7);
			setState(36);
			match(INT);
			setState(37);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PassActionContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(TaticBoardParser.INT, 0); }
		public PassActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_passAction; }
	}

	public final PassActionContext passAction() throws RecognitionException {
		PassActionContext _localctx = new PassActionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_passAction);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(39);
			match(T__8);
			setState(40);
			match(T__4);
			setState(41);
			match(INT);
			setState(42);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ShootActionContext extends ParserRuleContext {
		public ShootActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shootAction; }
	}

	public final ShootActionContext shootAction() throws RecognitionException {
		ShootActionContext _localctx = new ShootActionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_shootAction);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			match(T__9);
			setState(45);
			match(T__4);
			setState(46);
			match(T__10);
			setState(47);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\r2\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0001\u0000\u0001\u0000\u0001\u0000\u0004\u0000\u0010"+
		"\b\u0000\u000b\u0000\f\u0000\u0011\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0003\u0002\u001f\b\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0000\u0000\u0006\u0000"+
		"\u0002\u0004\u0006\b\n\u0000\u0000.\u0000\f\u0001\u0000\u0000\u0000\u0002"+
		"\u0015\u0001\u0000\u0000\u0000\u0004\u0017\u0001\u0000\u0000\u0000\u0006"+
		" \u0001\u0000\u0000\u0000\b\'\u0001\u0000\u0000\u0000\n,\u0001\u0000\u0000"+
		"\u0000\f\r\u0005\u0001\u0000\u0000\r\u000f\u0005\u0002\u0000\u0000\u000e"+
		"\u0010\u0003\u0002\u0001\u0000\u000f\u000e\u0001\u0000\u0000\u0000\u0010"+
		"\u0011\u0001\u0000\u0000\u0000\u0011\u000f\u0001\u0000\u0000\u0000\u0011"+
		"\u0012\u0001\u0000\u0000\u0000\u0012\u0013\u0001\u0000\u0000\u0000\u0013"+
		"\u0014\u0005\u0003\u0000\u0000\u0014\u0001\u0001\u0000\u0000\u0000\u0015"+
		"\u0016\u0003\u0004\u0002\u0000\u0016\u0003\u0001\u0000\u0000\u0000\u0017"+
		"\u0018\u0005\u0004\u0000\u0000\u0018\u0019\u0005\u0005\u0000\u0000\u0019"+
		"\u001a\u0005\f\u0000\u0000\u001a\u001e\u0005\u0006\u0000\u0000\u001b\u001f"+
		"\u0003\u0006\u0003\u0000\u001c\u001f\u0003\b\u0004\u0000\u001d\u001f\u0003"+
		"\n\u0005\u0000\u001e\u001b\u0001\u0000\u0000\u0000\u001e\u001c\u0001\u0000"+
		"\u0000\u0000\u001e\u001d\u0001\u0000\u0000\u0000\u001f\u0005\u0001\u0000"+
		"\u0000\u0000 !\u0005\u0007\u0000\u0000!\"\u0005\u0005\u0000\u0000\"#\u0005"+
		"\f\u0000\u0000#$\u0005\b\u0000\u0000$%\u0005\f\u0000\u0000%&\u0005\u0006"+
		"\u0000\u0000&\u0007\u0001\u0000\u0000\u0000\'(\u0005\t\u0000\u0000()\u0005"+
		"\u0005\u0000\u0000)*\u0005\f\u0000\u0000*+\u0005\u0006\u0000\u0000+\t"+
		"\u0001\u0000\u0000\u0000,-\u0005\n\u0000\u0000-.\u0005\u0005\u0000\u0000"+
		"./\u0005\u000b\u0000\u0000/0\u0005\u0006\u0000\u00000\u000b\u0001\u0000"+
		"\u0000\u0000\u0002\u0011\u001e";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}